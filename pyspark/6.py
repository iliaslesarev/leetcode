from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("app").getOrCreate()

data = [("A", 10), ("B", 20), ("C", 30), ("D", 40), ("E", 50), ("F", 15), ("G", 28), ("H", 54), ("I", 41), ("J", 86)]
df = spark.createDataFrame(data, ["Name", "Age"])

df.show()

df.approxQuantile("Age", [0.0, 0.25, 0.5, ])