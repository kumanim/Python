from pyspark.sql import SparkSession
from pyspark.sql.types import *

if __name__=="__main__":
    print('Data ingestion from local system system started...')

spark=SparkSession.builder.appName('Filesys-stream').getOrCreate()

input_csv_schema=StructType([
    StructField("star_rating", DoubleType(), True),
    StructField("title",StringType(),True),
    StructField("content_rating",StringType(),True),
    StructField("genre",StringType(),True),
    StructField("duration", IntegerType(),True),
    StructField("actors_list", StringType(),True)
])

stream_df=spark.readStream.format("csv").option("header","true").schema(input_csv_schema).load(path="/home/ubuntu/Downloads/imdb")

stream_df.printSchema()

stream_df_query=stream_df.writeStream.format("console").start()

stream_df_query.awaitTermination()

print('Scanning closed')