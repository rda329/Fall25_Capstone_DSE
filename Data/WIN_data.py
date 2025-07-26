from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("SpeedTest") \
    .master("local[*]") \
    .getOrCreate()

print("Spark started!")
spark.stop()