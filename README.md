# Introduction

Template project for running spark development locally with an IDE

# Dependencies

Requires spark installed locally, SPARK_HOME set and $SPARK_HOME/bin set on the path.
Also add the following to conf at `$SPARK_HOME/conf/spark_defaults.conf` in order to use delta lake.

```
spark.jars.packages               io.delta:delta-core_2.12:0.8.0
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


Exporting variables doesn't make for a great development experience so I recommend using the enviroment manager tools of your editor and for testing create a ./pytest.ini that looks like this:

```
[pytest]
env =
    blah=blah
```

**REMINDER: do NOT commit any files that contain security tokens**

Git ignore already contains an exclusion for pytest.ini


# Build

Build python wheel:
```
python setup.py sdist bdist_wheel
```

There is a CI build configured for this repo that builds on main origin on a private Azure DevOps service. It doesn't yet push to PyPi.

# Test

Dependencies for testing:
```
pip install --editable .
```

Run tests:
```
pytest
```

Test Coverage:
```
pytest --cov=spark_python_demo --cov-report=html
```

View the report in a browser:
```
./htmlcov/index.html
```


