from core.schema import product_category_tree, image_schema, product_specs_schema
from utils.format import format_arr, apply_mapping_attribute
from pyspark.sql.functions import col, udf
import ast

class Tasks:
    def __init__(self, data_frame):
        self.data_frame = data_frame

    def apply_prod_category_format(self):
        product_category_tree_udf = udf(lambda x:format_arr(ast.literal_eval(x)),product_category_tree)
        self.data_frame = self.data_frame.withColumn("product_category_tree", product_category_tree_udf(col("product_category_tree")))
    
    def apply_image_format(self):
        image_udf = udf(lambda x: ast.literal_eval(x), image_schema)
        self.data_frame = self.data_frame.withColumn("image", image_udf(col("image")))
    
    def apply_prod_specs_format(self):
        product_specifications_udf = udf(lambda x:apply_mapping_attribute(x),product_specs_schema) 
        self.data_frame = self.data_frame.withColumn("product_specifications", product_specifications_udf(col("product_specifications")))
    
    def apply_all(self):
        self.apply_prod_category_format()
        self.apply_image_format()
        self.apply_prod_specs_format()
    



