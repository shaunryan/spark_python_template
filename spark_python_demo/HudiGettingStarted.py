from .SparkContext import spark, log
from .AppConfig import get_hudi_data_root

def go():

    log.info("starting hudi exmaple")

    log.info("Setting Up Hudi Example")
    tableName = "hudi_trips_cow"
    basePath = f"{get_hudi_data_root()}hudi_trips_cow"
    dataGen = spark._jvm.org.apache.hudi.QuickstartUtils.DataGenerator()
    

    # Insert data
    # Generate some new trips, load them into a DataFrame and write the DataFrame into the Hudi table as below.
    log.info("Hudi Insert Data")
    inserts = spark._jvm.org.apache.hudi.QuickstartUtils.convertToStringList(dataGen.generateInserts(10))
    df = spark.read.json(spark.sparkContext.parallelize(inserts, 2))
    
    hudi_options = {
    'hoodie.table.name': tableName,
    'hoodie.datasource.write.recordkey.field': 'uuid',
    'hoodie.datasource.write.partitionpath.field': 'partitionpath',
    'hoodie.datasource.write.table.name': tableName,
    'hoodie.datasource.write.operation': 'upsert',
    'hoodie.datasource.write.precombine.field': 'ts',
    'hoodie.upsert.shuffle.parallelism': 2, 
    'hoodie.insert.shuffle.parallelism': 2
    }

    df.write.format("hudi") \
    .options(**hudi_options) \
    .mode("overwrite") \
    .save(basePath)

    # Query
    # This query provides snapshot querying of the ingested data. Since our partition path (region/country/city) is 3 levels nested from base path we ve used load(basePath + "/*/*/*/*"). 
    # Refer to Table types and queries for more info on all table types and query types supported.
    # Load the data files into a DataFrame.

    log.info("Hudi Insert Data")
    tripsSnapshotDF = spark \
    .read \
    .format("hudi") \
    .load(basePath + "/*/*/*/*")
    # load(basePath) use "/partitionKey=partitionValue" folder structure for Spark auto partition discovery

    tripsSnapshotDF.createOrReplaceTempView("hudi_trips_snapshot")

    spark.sql("select fare, begin_lon, begin_lat, ts from  hudi_trips_snapshot where fare > 20.0").show()
    spark.sql("select _hoodie_commit_time, _hoodie_record_key, _hoodie_partition_path, rider, driver, fare from  hudi_trips_snapshot").show()

    spark.stop()