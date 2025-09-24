from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("app").getOrCreate()

list_A = [1, 2, 3, 4, 5]
list_B = [4, 5, 6, 7, 8]


rdd_A = spark.sparkContext.parallelize(list_A)
rdd_B = spark.sparkContext.parallelize(list_B)

rdd = rdd_A.subtract(rdd_B).collect()

print(rdd)

spark.stop()