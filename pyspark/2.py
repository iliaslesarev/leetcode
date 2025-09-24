from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import monotonically_increasing_id, row_number

spark = SparkSession.builder.appName("app").getOrCreate()

df = spark.createDataFrame([
    ("Alice", 1),
    ("Bob", 2),
    ("Charlie", 3)
], ["Name", "Value"])

w = Window.orderBy(monotonically_increasing_id())

(df
 .withColumn("index", row_number().over(w) - 1)
 .show())

spark.stop()
