import logging

from config.session import start_spark
from config.loader import Loader
from environments import mod_path
from core.schema import product_schema
from core.tasks import Tasks, write_df_to_sql

def main():
    full_path = mod_path / "env.yaml"
    logging.info(full_path)
    with open(str(full_path), 'r') as file:
        contents = Loader(file).get_contents()
        sql_context, config_dict = start_spark(
            app_name=contents.app_name,
            master=contents.master,
            log_level=contents.log_level
        )

        data = sql_context.read.csv(
            contents.source_file, 
            schema=product_schema, 
            inferSchema = True, 
            header = True, 
            escape='"'
        ).cache()
        tasks = Tasks(data)
        tasks.apply_all()
        data = tasks.data_frame
        write_df_to_sql(data)



if __name__ == "__main__":
    main()