from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('TrailerFlix').getOrCreate()
client = (
    spark.readStream
    .format('socket')
    .option('host', 'localhost')
    .option('port', 9009)
    .load()
)

query = (
    client.writeStream
    .outputMode('append')
    .format('console')
    .start()
)

query.awaitTermination()
