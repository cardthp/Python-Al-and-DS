import requests
import mysql.connector
import pandas as pd

#API
response = requests.get('http://localhost/marketPurchase')
response = response.json()
timestamp = int(response['timestamp']) #2021-01-01
productprice = int(response['productPrice']) #1001

cnx = mysql.connector.connect(
    host = "db",
    database = "ri_db",
    user = "test",
    password = ""
)

cursor = cnx.cursor()
sql = "SELECT * FROM currency"

cursor.execute(sql)

result = cursor.fetchall()

sql_dict = {int(n[0]):int(n[1]) for n in result}
timestamp_list = [int(n[0]) for n in result]

for i in range(len(timestamp_list)) :
    if timestamp == timestamp_list[i] :
        exchange = sql_dict[timestamp_list[i]]
        break
    elif timestamp < timestamp_list[i] :
        exchange = sql_dict[timestamp_list[i-1]]
        break
    else :
        exchange = 1
        
print(exchange*productprice)
