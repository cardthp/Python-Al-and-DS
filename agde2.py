import pandas as pd

#mysql
base1 = mysql.connector.connect(
    host = "",
    database
    user 
    passw
)

sql = "SELECT * FROM currency"
cursor = base1.cursor().execute(sql)
result = cursor.fetchall()

table = pd.DataFrame(result)

#API
response = requests.get(url)
response = response.json()
timestamp = int(response['timestamp']) #2021-01-01
product = int(response['product']) #1001

table = pd.read_csv("test2.csv")
result2 = table[table['timestamp'] <= 7]
# result2 = table[table['timestamp'] <= timestamp]
result3 = result2['timestamp'].max()
result4 = table[table['timestamp'] == result3]
result5 = result4['price'].values[0]
print(result5*10)



# import json
# f = open('test.json',)
 
# data = json.load(f)
# print(data)
# for i in data:
#     #print(i)
#     timestamp = int(i['b'])
#     print(timestamp)
