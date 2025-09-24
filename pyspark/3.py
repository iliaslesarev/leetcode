from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("app").getOrCreate()

list1 = ["a", "b", "c", "d"]
list2 = [1, 2, 3, 4]

df = spark.createDataFrame(
    list(zip(list1, list2)),
    ["letter", "number"]
)

df.show()

spark.stop()
