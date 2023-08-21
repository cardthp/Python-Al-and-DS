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

table = pd.DataFrame(result)
table.columns = ['timestamp', 'exchangeRate'] #detect columns on dataframe

#API
response = requests.get('http://localhost/marketPurchase')
response = response.json()
timestamp = int(response['timestamp']) #2021-01-01
productprice = int(response['productPrice']) #1001

result2 = table[table['timestamp'] <= timestamp] #find only timestamp which more than API timestamp
result3 = result2['timestamp'].max()
result4 = table[table['timestamp'] == result3]
exchange = result4['exchangeRate'].values[0]
print(exchange*productprice)