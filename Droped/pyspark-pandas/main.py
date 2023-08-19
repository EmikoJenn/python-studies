import pyspark
import pandas as pd

pd.read_csv('data.csv')

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Practise').getOrCreate()

# df_pyspark = spark.read.csv('data.csv')
df_pyspark = spark.read.csv("data.csv", inferSchema=True, header=True)
# type(df_pyspark)
# df_pyspark.head(3)
df_pyspark.printSchema()
df_pyspark.select(['Name', 'Age']).show()