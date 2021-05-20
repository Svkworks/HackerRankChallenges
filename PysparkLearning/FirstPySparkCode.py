import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Test").master("local[*]").getOrCreate()

rdd1 = spark.sparkContext.parallelize([1,2,3,4,5])

rdd2 = rdd1.map(lambda x : x*4)

print(rdd2.takeOrdered(5))
