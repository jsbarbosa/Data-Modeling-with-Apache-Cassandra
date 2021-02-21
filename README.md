# Data Modeling with Apache Cassandra

Sparkify is a music streaming app, who wants to analyze the data they've been collecting on songs and user activity.

Data is originally stored in CSV files, but in order to analyse it an Apache Cassandra database was built. Since queries model the database, three denormalized tables are build with the ETL.

# ETL
The logical process by which the data is uploaded to the database is composed by three steps:

## Creating tables
In order to create the `KEYSPACE` and the corresponding tables the following process must be run:
```
python create_tables.py
```

## Transforming data
Since the original data has a different schema, a transformation of the dataset is made with `create_csv.py` which stores transformed data as CSV

## ETL
Populates the entire database by using the data available in `event_datafile_new.csv`

# Project requirements
Requirements can be found in `requirements.txt`

# Docker
A container for the whole application can be found in `docker/`

## Running
```
cd docker/
sudo docker-compose up
```

