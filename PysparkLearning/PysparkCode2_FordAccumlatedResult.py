from pyspark.sql import SparkSession
from pyspark.sql.column import Column
from pyspark.sql.functions import sum, col, dense_rank, lag, lead, when
from pyspark.sql.types import Row
from pyspark.sql.window import Window

spark = SparkSession.builder.appName("Test").master("local[*]").getOrCreate()


filePath = spark.sparkContext.textFile("/Users/saim/Documents/Svk_Work/Learning_Documents/Spark_PySpark/ford_escort.csv")\

rddHeader = filePath.first()

rdd1 = filePath.filter(lambda  x : x != rddHeader)\
    .map(lambda x : x.split(","))\
    .filter(lambda x : str('\"') not in x)\
    .map(lambda  x : Row(year=x[0],milage=x[1],price=x[2]))\
    .toDF()

#rdd1.show(truncate=True)
rdd2 = rdd1.groupby(rdd1["year"]) \
    .agg(sum(rdd1["milage"]).alias("Sum_Of_milage"),
         sum(col("price")).alias("sum_of_price"))\
    .withColumn("Previous_year_prices",lag(col("sum_of_price"),1).over(Window.orderBy(col("year"))))\
    .withColumn("diff",when((col("sum_of_price")-col("Previous_year_prices"))<0,"Loss").otherwise("Profit"))\
    .sort(col("year"), ascending=True)\
    #.show(truncate=False)

rdd2.write.mode(saveMode="overwrite").json("/Users/saim/Documents/Svk_Work/Learning_Documents/Spark_PySpark/PySparkCodeResult")