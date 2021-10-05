# Sertis DE take-home test

## Overview

We have a system that collects transactional data and stores them as CSV files. A sample input can be found in `data/transaction.csv`. Imagine that the amount of transactions was huge. Your task is to build an ETL pipeline that aggregates the transactions by user id and stores the results to another database that will be used to serve interactive queries.

## Requirements

Aggregated customer data needs to be stored in PostgreSQL 13 database. The schema of the target table should be:

| Column      | Description |
| ----------- | ----------- |
| customer_id      | Column `custId` from source data       |
| favourite_product   | Column `productSold` from source data which has greatest total units sold for this customer |
| longest_streak   | The longest period of consecutive days when this customer made purchases. For example, if the customer bought items on 2011-08-10, 2011-08-11, 2011-08-14, 2011-08-15 and 2011-08-16, Value of `longest_streak` would be 3.  |


The ETL tool needs to be a Python command line tool that accepts the following arguments:

| Argument      | Description |
| ----------- | ----------- |
| source      | Path to the source file       |
| database   | Database name for inserting data |
| table   | Table name for inserting data  |

As we are using Poetry, the application can be executing using:
```shell
poetry run python main.py \
  --source /opt/data/transaction.csv \
  --database warehouse \
  --table customers
```


## Instructions

### Part 1. Implementation

* Use `main.py` as an entry point to your application. Feel free to structure your application as you find fit and add modules and packages if necessary. Use the provided Apache Spark version for implementing the pipeline. File `main.py` contains snippets on how to get started. Feel free to use either Spark DSL (PySpark) or SQL syntax for transformations.
* Dockerized Spark is provided in the compose file. Use this when building the `SparkSession`.
* Add a docker container for PostgreSQL to the compose file. The ETL pipeline should write its output to this database.
* Dockerize your application into a Docker file and add a `docker-compose` service for it. It is recommended to use the [official Python 3.9 image](https://hub.docker.com/_/python) as a base. Hint: Either Java 8 or Java 11 is required to run Spark.
* Add an integration test to your project that runs the ETL pipeline using the given sample input file `data/transaction.csv` and writes it to PostgreSQL. Assert values of `longest_streak` and `favourite_product` for `customer_id=0023938`. It is up to your design if you want to run the tests inside or outside docker.
* Remember to ask Google. Required tools Python, Poetry, Spark, Docker and PostgreSQL are all popular tools with tons of information online.
* If you get stuck, feel free to take shortcuts by changing requirements and let us know what you changed. For example, if you want to skip using PostgreSQL, you can just use local filesystem as a target.

Submission: Implement the requirements in this Git repository and create a [patch file](https://git-scm.com/docs/git-format-patch) for the changes. Include the patch file in your submitted documents.

### Part 2. Deployment

This task does not have to be implemented, but we would like you to propose a solution on how this can be achieved. Choose one of the major cloud platforms, Amazon Web Services, Google Cloud Platform or Microsoft Azure as a basis of your solution and use services provided by the chosen platform. Describe how you would implement the following system in the cloud of your choice:
* The source data is stored in on-premise RDBMS. The schema is like the transactional data in Part 1.
* A daily ETL pipeline needs to ingest the data, do the same transformations as in Part 1 and store the output in the cloud where it can be queried.
* The solution needs to be scalable in terms of data amount.

Optional: Propose solutions for monitoring, logging and automated notifications.

Submission: Explanation of the proposed solution, chosen tools/frameworks, justification on why you chose them, and any other supporting documentation in a PDF format. Feel free to make your own assumptions (e.g. feel free to use any services in the chosen cloud platform) and be as creative as you want with your answer. Remember to cover the requirements i.e. how the data is moved to the cloud, how the aggregations are calculated in your proposed solution and how scalability is achieved.

## Verifying ETL pipeline

As our pipeline is dockerized, it is easy to execute and verify the output. Assuming the pipeline is called `etl` in `docker-compose`, we can use `docker-compose` to run the pipeline:
```shell
docker-compose build
docker-compose run etl poetry run python main.py \
  --source /opt/data/transaction.csv \
  --database warehouse \
  --table customers
```
After this we should be able to query the aggregated data from PostgreSQL (assuming the database is called `db` in `docker-compose`):
```shell
docker-compose exec db psql --user postgres -d warehouse \
  -c 'select * from customers limit 10'
```
