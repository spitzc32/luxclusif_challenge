from pyspark.sql.types import StructType, StructField, StringType, DateType, DecimalType, BooleanType, MapType, ArrayType

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