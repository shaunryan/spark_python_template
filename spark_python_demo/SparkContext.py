import os

from pyspark.sql import SparkSession
from .AppConfig import get_log_level


spark = SparkSession\
    .builder\
    .master("local[2]")\
    .appName("demo")\
    .getOrCreate()

log_level = get_log_level()
spark.sparkContext.setLogLevel(log_level)


_log4jLogger = spark._jvm.org.apache.log4j
log = _log4jLogger.LogManager.getRootLogger()

