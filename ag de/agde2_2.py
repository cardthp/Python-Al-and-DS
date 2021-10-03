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

cursor = base1.cursor()
sql = "SELECT * FROM currency"

cursor.execute(sql)

result = cursor.fetchall()
table = pd.DataFrame(result)
table.columns = ['timestamp', 'exchangeRate']

#API
response = requests.get('http://localhost/marketPurchase')
response = response.json()
timestamp = int(response['timestamp']) #2021-01-01
productprice = int(response['productPrice']) #1001

result2 = table[table['timestamp'] <= timestamp]
result3 = result2['timestamp'].max()
result4 = table[table['timestamp'] == result3]
exchange = result4['exchangeRate'].values[0]
print(exchange*productprice)