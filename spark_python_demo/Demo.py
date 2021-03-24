
import random
# from pyspark import SparkContext, sql
from pyspark.sql import functions as F
from pyspark.sql.types import BooleanType
from .SparkContext import spark, log

#simple filter function
@F.udf(returnType=BooleanType())
def inside(p):

    x, y = random.random(), random.random()
    return x*x + y*y < 1

def execute():

    log.info("starting")
    
    NUM_SAMPLES = 1000000

    count = spark.range(0, NUM_SAMPLES).filter(inside("id")).count()
    log.info("Pi is roughly %f" % (4.0 * count / NUM_SAMPLES))

    spark.stop()



