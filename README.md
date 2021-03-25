# Introduction

Template project for running spark development locally with an IDE.
Primarily serves as local python build template and a playground setup for hudi and delta lake.

Requires a spark standalone or cluster. Please see dependencies.

# Dependencies

To work locally it requires spark installed locally, SPARK_HOME set and $SPARK_HOME/bin set on the path.
Also add the following to conf at `$SPARK_HOME/conf/spark_defaults.conf` in order to use delta lake and hudi.

For Delta lake:
```
spark.jars.packages               io.delta:delta-core_2.12:0.8.0
spark.sql.extensions              io.delta.sql.DeltaSparkSessionExtension
spark.sql.catalog.spark_catalog   org.apache.spark.sql.delta.catalog.DeltaCatalog
```

For Hudi:
```
spark.serializer                 org.apache.spark.serializer.KryoSerializer

spark.jars.packages               org.apache.parquet:parquet-hive-bundle:1.11.1,org.apache.hudi:hudi-spark-bundle_2.12:0.7.0,org.apache.spark:spark-avro_2.12:3.1.1
```

and for both:

```
spark.serializer                 org.apache.spark.serializer.KryoSerializer

spark.jars.packages               io.delta:delta-core_2.12:0.8.0,org.apache.parquet:parquet-hive-bundle:1.11.1,org.apache.hudi:hudi-spark-bundle_2.12:0.7.0,org.apache.spark:spark-avro_2.12:3.1.1
spark.sql.extensions              io.delta.sql.DeltaSparkSessionExtension
spark.sql.catalog.spark_catalog   org.apache.spark.sql.delta.catalog.DeltaCatalog
```

# Setup

Create virual environment and install dependencies for local development:

```
python3.7 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
pip install -r dev_requirements.txt
```

Note the variables in .env. Adjust them accordingly.

```
ENVIRONMENT=local
HUDI_DATAROOT="file:///Users/shaunryan/code/spark_python_template/data/hudi/"
DELTA_DATAROOT="file:///Users/shaunryan/code/spark_python_template/data/delta/"
LOG_LEVEL=WARN
```




# Run

It's a vscode project. The .vscode/launch.json is included in the repo.
Just hit F5 to run main.py that will call into the module `spark_python_demo`

