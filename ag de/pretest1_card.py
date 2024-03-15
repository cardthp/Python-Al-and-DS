import requests
import mysql.connector
import pandas as pd

#mysql
base1 = mysql.connector.connect(
    host = "db",
    database = "ri_db",
    user = "test",
    password = ""
)

cursor = base1.cursor() #cursor means you can execute operations such as SQL statements
cursor.execute("SELECT * FROM currency")

result = cursor.fetchall()

table_sql = pd.DataFrame(result)
table_sql.columns = ['timestamp', 'exchangeRate'] #detect columns on dataframe

#API
response = requests.get('http://localhost/marketPurchase')
response = response.json()
timestamp_API = int(response['timestamp']) #2021-01-01
productprice = int(response['productPrice']) #1001

#this step for find current exchange (lasted timestamp)
list_timestamp_sql = table_sql[table_sql['timestamp'] <= timestamp_API] #filter only timestamp which more than API timestamp
result_timestamp_sql_max = list_timestamp_sql['timestamp'].max()

#this step for gathering exchange rate (lasted timestamp)
timestamp_for_exchange_rate = table_sql[table_sql['timestamp'] == result_timestamp_sql_max]
current_exchange_rate = timestamp_for_exchange_rate['exchangeRate'].values[0]

print(current_exchange_rate*productprice)