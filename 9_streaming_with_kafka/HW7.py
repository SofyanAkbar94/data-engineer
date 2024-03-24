import pyspark
from pyspark.sql import SparkSession
from pyspark.sql import types
from pyspark.sql import functions as F

pyspark_version = pyspark.__version__
kafka_jar_package = f"org.apache.spark:spark-sql-kafka-0-10_2.12:{pyspark_version}"

spark = SparkSession.builder.master("local[*]").appName('GreenTripsConsumer').\
    config("spark.jars.packages", kafka_jar_package).getOrCreate()

# Assuming you have a streaming DataFrame named `green_stream` representing your stream of data
green_stream = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "green-trips") \
    .option("startingOffsets", "earliest") \
    .load()

schema = types.StructType([
    types.StructField('lpep_pickup_datetime', types.StringType(), True),
    types.StructField('lpep_dropoff_datetime', types.StringType(), True),
    types.StructField('PULocationID', types.IntegerType(), True),
    types.StructField('DOLocationID', types.IntegerType(), True),    
    types.StructField('passenger_count', types.DoubleType(), True),
    types.StructField('trip_distance', types.DoubleType(), True),
    types.StructField('tip_amount', types.DoubleType(), True)
])

green_stream = green_stream \
    .select(F.from_json(F.col("value").cast('STRING'), schema).alias("data")) \
    .select("data.*") \
    .withColumn("timestamp", F.current_timestamp()) # Add timestamp column

popular_destinations = green_stream \
    .groupBy(F.window(F.col("timestamp"), "5 minutes"), F.col("DOLocationID")) \
    .count() \
    .orderBy(F.desc("count")) \
    .select("window", "DOLocationID", "count")

query = popular_destinations \
    .writeStream \
    .outputMode("complete") \
    .format("console") \
    .option("truncate", "false") \
    .start()

query.awaitTermination()

print(query)
