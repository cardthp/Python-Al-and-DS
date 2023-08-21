import requests
import mysql.connector
import pandas as pd

#API
response = requests.get('http://localhost/marketPurchase')
response = response.json()
timestamp = int(response['timestamp']) #2021-01-01
productprice = int(response['productPrice']) #1001

#connect my sql
cnx = mysql.connector.connect(
    host = "db",
    database = "ri_db",
    user = "test",
    password = ""
)

cursor = cnx.cursor() #cursor means you can execute operations such as SQL statements
cursor.execute("SELECT * FROM currency")

result = cursor.fetchall() #call data to show

sql_dict = {int(n[0]):int(n[1]) for n in result}
timestamp_list = [int(n[0]) for n in result]

for i in range(len(timestamp_list)) : #this step for find current exchange (lasted timestamp)
    if timestamp == timestamp_list[i] :
        exchange = sql_dict[timestamp_list[i]]
        break
    elif timestamp < timestamp_list[i] :
        exchange = sql_dict[timestamp_list[i-1]]
        break
    else :
        exchange = 1
        
print(exchange*productprice)
