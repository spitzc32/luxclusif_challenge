from pyspark.sql.types import StructType, StructField, StringType, DateType, DecimalType, BooleanType, MapType, ArrayType
from pyspark.sql.functions import col, udf
from pyspark.sql.functions import to_json

import numpy as np
import ast


def tree_mapper(categories: str):
    """
    Maps and strips the productname from the category tree

    :param categories: string of category tree the product has
    """
    return [category.strip() for category in categories.split(">>")][:-1]

def format_arr(arr: list):
    """
    Flatten and map items under category tree to get a list of categories

    :param arr: array of category tree
    """
    items = np.array([tree_mapper(item) for item in arr][:-1])
    flat =items.flatten()
    return flat.tolist()

def key_val_extractor(iterable: dict):
    if "key" in iterable:
        return {iterable["key"]: iterable["value"]}
    return {}

def format_str_to_dict(item: str):
    return ast.literal_eval(item.replace("=>", ":"))

def apply_mapping_attribute(item: str):
    """
    validate and flatten attributes for product specifics

    :param iterable: dictionary of product_specification
    """
    items = format_str_to_dict(item)
    mapping = {}
    if "product_specification" in items.keys():
        #validated_items = ProductSpecs(**item)
        for item in items["product_specification"]:
                mapping.update(key_val_extractor(item))

    return mapping

product_schema = StructType([
    StructField("uniq_id", StringType()),
    StructField("crawl_timestamp", DateType()),
    StructField("product_url", StringType()),
    StructField("product_name", StringType()),
    StructField("product_category_tree",StringType() ),
    StructField("pid", StringType()),
    StructField("retail_price", DecimalType(precision=38, scale=2)),
    StructField("discounted_price", DecimalType(precision=38, scale=2)),
    StructField("image", StringType()),
    StructField("is_FK_Advantage_product", BooleanType()),
    StructField("description", StringType()),
    StructField("product_rating", StringType()),
    StructField("overall_rating", StringType()),
    StructField("brand", StringType()),
    StructField("product_specifications", StringType())
])

product_category_tree = ArrayType(StringType())
image_schema = ArrayType(StringType())
product_specs_schema = MapType(keyType=StringType(), valueType=StringType())


class Tasks:
    def __init__(self, data_frame):
        self.data_frame = data_frame

    def apply_prod_category_format(self):
        print("Applying product category format..")
        product_category_tree_udf = udf(lambda x:format_arr(ast.literal_eval(x)),product_category_tree)
        self.data_frame = self.data_frame.withColumn("product_category_tree", product_category_tree_udf(col("product_category_tree")))
    
    def apply_image_format(self):
        print("Applying image format..")
        image_udf = udf(lambda x: ast.literal_eval(x), image_schema)
        self.data_frame = self.data_frame.withColumn("image", image_udf(col("image")))
    
    def apply_prod_specs_format(self):
        print("Applying product_specifications format..")
        product_specifications_udf = udf(lambda x:apply_mapping_attribute(x),product_specs_schema) 
        self.data_frame = self.data_frame.withColumn("product_specifications", product_specifications_udf(col("product_specifications")))
        self.data_frame = self.data_frame.withColumn("product_specifications", to_json(col("product_specifications")))

        self.data_frame.printSchema()
    
    def apply_all(self):
        self.apply_prod_category_format()
        self.apply_image_format()
        self.apply_prod_specs_format()
        print("Done application. Now proceeding with writing to db...")
    
def write_df_to_sql(data_frame):
    print("Writing to database...")
    data_frame
    data_frame.select("*").write.format("jdbc") \
    .option("url", "jdbc:postgresql://host.docker.internal:5432/postgres") \
    .option("driver", "org.postgresql.Driver").option("dbtable", "products_spark") \
    .option("user", "prod_admin").option("password", "prod_admin").mode("overwrite").save()


