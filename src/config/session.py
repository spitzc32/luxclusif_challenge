from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext

from typing import Optional
from config.loader import Loader

def start_spark(
    app_name: str ='my_spark_app', 
    master: Optional[str] ='local[*]',
    spark_config="",
    log_level:str =""
):
    conf = SparkConf().setAppName(app_name).setMaster(master)
    sc = SparkContext(conf=conf)
    sql_context = SQLContext(sc)
    config_dict = None
    sc.setLogLevel(log_level)

    if len(spark_config) > 0:
        config_dict = Loader(spark_config).get_contents()
    
    return sql_context, config_dict


