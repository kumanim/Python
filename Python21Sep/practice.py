# Spark Streaming Application
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

if __name__ == "__main__":
    print('Streaming ingestion is started....')

spark = SparkSession.builder.appName('Stream').getOrCreate()

stream_df = spark.readStream.format("socket").option("host","127.0.0.1").option("port","1400").load()

print(stream_df.isStreaming)
stream_df.printSchema()

stream_words_df=stream_df.select(explode(split("value",' ')).alias("word"))

stream_word_count_df=stream_words_df.groupby("word").count()

write_query=stream_word_count_df.writeStream.outputMode("update").format("console").start()

write_query.awaitTermination()

print('Streaming ended!')