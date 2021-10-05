#import lib
from pyspark.sql import SparkSession
import pandas as pd


#Create SparkSession

#for Create SparkSeesion on Localhost
#spark: SparkSession = SparkSession.builder.master("local[*]").getOrCreate()

#for Create SparkSeesion via docker-compose
spark: SparkSession = SparkSession.builder.master('spark://spark:7077').getOrCreate()

    
#############################################################################################
#Step1 : Get data transaction file to Spark dataframe
df = spark.read.csv('data/transaction.csv', sep='|', header=True, inferSchema=True)

"""Select customerID before beacuse it will reduce runtime to query the next process 
or if you don't want to hardcode on customerID it can use parameter that get input data via keyboard by create variable
"""
df_SelectCustomer = df.where(df['custId'] == '0023938')

#Create view that filtered a customerID
df_SelectCustomer.createOrReplaceTempView('transaction_SelectCustomer')


#############################################################################################
#Step2 : Query view that filter a customerID to find longest_streak by maxdate minus mindate
df_longest_streak = spark.sql("""
SELECT custId,
DATEDIFF(to_date(max(transactionDate), 'yyyy-MM-dd'),to_date(min(transactionDate), 'yyyy-MM-dd')) AS DateDiff_InDays
FROM transaction_SelectCustomer
GROUP BY custId
""")

#Create view that show longest_streak 
df_longest_streak.createOrReplaceTempView('view_longest_streak')


#############################################################################################
#Step3 : Query view that filter a customerID to find favourite_product it have 3 parts
#For part1 to find favourite_product it need to find unitsSold from each productSold
df_favourite_product_sumUnitsSold = spark.sql("""
SELECT custId,
productSold,
SUM(unitsSold) AS unitsSold
FROM transaction_SelectCustomer
GROUP BY custId,productSold
""")

df_favourite_product_sumUnitsSold.createOrReplaceTempView('view_favourite_product_sumUnitsSold')

#For part2 to find favourite_product it need to descending unitsSold by create Row_Number
df_favourite_product_sumUnitsSold_DESC = spark.sql("""
SELECT custId,
productSold,
unitsSold,
ROW_NUMBER() OVER (PARTITION BY custId ORDER BY unitsSold DESC) AS row_num
FROM view_favourite_product_sumUnitsSold
""")

df_favourite_product_sumUnitsSold_DESC.createOrReplaceTempView('view_favourite_product_sumUnitsSold_DESC')

#For part3 to find favourite_product it need to select productSold that top1 from Row_Number
df_favourite_product = spark.sql("""
SELECT custId,
productSold,
unitsSold
FROM view_favourite_product_sumUnitsSold_DESC
WHERE row_num = 1
""")

#Create view that show favourite_product
df_favourite_product.createOrReplaceTempView('view_favourite_product')


#############################################################################################
#Step4 : Inner join customerID to find longest_streak and favourite_product from view longest_streak and favourite_product
df_longest_streak_favourite_product = spark.sql("""
SELECT f.custId AS customer_id,
f.productSold AS favourite_product,
l.DateDiff_InDays AS longest_streak
FROM view_longest_streak l
INNER JOIN view_favourite_product f
ON l.custId = f.custId
""")


#############################################################################################
#Step5 : Convert to Pandas Dataframe to Prepare send csv to output file 
pd_df_longest_streak_favourite_product = df_longest_streak_favourite_product.toPandas()
pd_df_longest_streak_favourite_product.to_csv('result.csv', index = False)



#############################################################################################
#Explain about parts that would like to change a requirements
"""
I have get stuck on the step to write data to Postgressql
    Explain: I have prepare to created table on PostgresSql on docker-compose file
if you run docker-compose you will found customers table on warehouse database and I separate problem that can't
write data to Postgressql for 2 scenario
"""

"""
# #Scenario1
I was stuck on this step to write data to Postgressql because error "java.sql.SQLException: No suitable driver"
I try to find information each other user was suggest to download Spark JDBC then move it to jars location of Spark file
and I try to that way and it was unresolved so in this case I would like to changed the requirements and output to the csv 
format that was attached in a zip file
"""

# PSQL_SERVERNAME = "postgres"
# PSQL_PORTNUMBER = 5432
# PSQL_DBNAME = "postgres"
# PSQL_USERNAME = "admin"
# PSQL_PASSWORD = "password"
# TABLE_CUSTOMER = "customer"

# URL = f"jdbc:postgresql://{PSQL_SERVERNAME}/{PSQL_DBNAME}"
# print(URL)

# df_longest_streak_favourite_product.write \
#     .format("jdbc") \
#     .option("url",URL) \
#     .option("dbtable",TABLE_CUSTOMER) \
#     .option("user",PSQL_USERNAME) \
#     .option("password",PSQL_PASSWORD) \
#     .save()


"""
# #Scenario2
I try to use psycopg2 and sqlalchemy lib.I found this problem that have issue from can't connect to Postgressql 
and it was showed "invaild password".Although try input correctly value from docker-compose
"""

# import psycopg2
# from sqlalchemy import create_engine

# # Create Engine
# engine = create_engine("postgresql+psycopg2://postgres:password@localhost:5432/warehouse?client_encoding=utf8")
# # Save result to the database via engine
# pd_df_longest_streak_favourite_product.to_sql('customers', engine, index=False, if_exists='replace')