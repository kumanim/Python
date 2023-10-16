from pyspark.sql import SparkSession
from pyspark.sql.functions import *
if __name__ == "__main__":
    print('Streaming ingestion is started....')
spark=SparkSession.builder.appName('Filesys-stream').getOrCreate()
spark=SparkSession.builder.appName('Scot').getOrCreate()
stream_dataf = spark.readStream.format('socket').option("host", "127.0.0.1").option("port", "1500").load(path="/home/ubuntu/Downloads/imdb_1000.csv")
print(stream_dataf.isStreaming)
stream_dataf.printSchema()