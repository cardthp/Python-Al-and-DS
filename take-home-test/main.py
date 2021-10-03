"""Entry point for the ETL application

Sample usage:
docker-compose run etl poetry run python main.py \
  --source /opt/data/transaction.csv \
  --database warehouse
  --table transactions
"""

from pyspark.sql import SparkSession

#spark: SparkSession = SparkSession.builder.master('spark://spark:7077').getOrCreate()
spark: SparkSession = SparkSession.builder.master("local[*]").getOrCreate()

# TODO: implement the pipeline. Remove the lines below, they are there just to get started.
#  Feel free to use either Spark DSL (PySpark) or Spark SQL syntax.
#  Both examples do the same, group by transactionId and calculate the sum of `unitsSold`.
# df = spark.read.csv('path/to/my/file/transaction.csv', sep='|', header=True, inferSchema=True)
# print(df)
# #################################################################
# # Spark DSL example
# df.groupBy('transactionId').sum('unitsSold').show()
# #################################################################

# #################################################################
# # Spark SQL example
# df.createOrReplaceTempView('transaction')
# spark.sql("""
# select transactionId, sum(unitsSold)
# from transaction
# group by transactionId
# """).show()
# #################################################################
