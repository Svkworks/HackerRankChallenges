from pyspark.sql import SparkSession
import Pyspark_Constants
from azure.storage.blob import *

#"""
#1. Create Azure Blob Storage Account and save STORAGE_NAME,SECRET_ACCESS_KEY somewhere
#2. Add hadoop-azure and azure-storage jars to your /spark/jars/. folder
#3. If it is pyspark add jetty-util jar to /spark/jars/. folder
#4. Add Storage_name and Access_key details in core-site.xml in hadoop/etc/ folder (optional)
#5. Follow the below steps to accecss the files
#"""


SECRET_ACCESS_KEY = Pyspark_Constants.SECRET_ACCESS_KEY
STORAGE_NAME = Pyspark_Constants.STORAGE_NAME

CONTAINER = "inputstorage1"
FILE_NAME = "movies.csv"


spark = SparkSession.builder.appName("Azure_PySpark_Connectivity")\
                    .master("local[*]")\
                    .getOrCreate()

fs_acc_key = "fs.azure.account.key." + STORAGE_NAME + ".blob.core.windows.net"
#spark.conf.set("spark.hadoop.fs.wasb.impl", "org.apache.hadoop.fs.azure.NativeAzureFileSystem")
#spark.conf.set("fs.wasbs.impl", "org.apache.hadoop.fs.azure.NativeAzureFileSystem")
spark.conf.set(fs_acc_key, SECRET_ACCESS_KEY)

path = "wasbs://inputstorage1@azuresvkstorageaccount.blob.core.windows.net/"
df = spark.read.csv(path+"movies.csv")
df.show(20,True)