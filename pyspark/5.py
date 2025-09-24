from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("app").getOrCreate()
sc = spark.sparkContext


list_A = [1, 2, 3, 4, 5]
list_B = [4, 5, 6, 7, 8]

rdd_A = sc.parallelize(list_A)
rdd_B = sc.parallelize(list_B)

sub_A = rdd_A.subtract(rdd_B)
sub_B = rdd_B.subtract(rdd_A)

print(sub_A.union(sub_B).collect())
