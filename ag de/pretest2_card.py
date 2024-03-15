import pandas as pd
import csv
import collections

df = pd.read_csv("data.csv")

#1 Get No. of Customer
customer_num = len(df['ID'].unique())
print("Total customers:")
print(customer_num)

#2 Get No. of Customer each City (Sort by city name ASC)
print("Customers by city:")
city = df.groupby('CITY').ID.nunique().reset_index()
city_sorted = city.sort_values(by=['CITY'])
for i, row in city_sorted.iterrows():
    print("{}: {}".format(row['CITY'],row['ID']))

#3 Get No. of Customer each Country (Sort by country name ASC)
print("Customers by country:")
city = df.groupby('COUNTRY').ID.nunique().reset_index()
city_sorted = city.sort_values(by=['COUNTRY'])
for i, row in city_sorted.iterrows():
    print("{}: {}".format(row['COUNTRY'],row['ID']))

#4 Which country has largest customers contract singed in and How many customers contract singed in
print("Country with the largest number of customers' contracts:")
country_singedin = df[['COUNTRY','CONTRCNT']].groupby('COUNTRY').sum().reset_index()
country_singedin2 = country_singedin['CONTRCNT'].max()
country_singedin3 = country_singedin[country_singedin['CONTRCNT'] == country_singedin2]
country_singedin_sorted = country_singedin3.sort_values(by=['COUNTRY'], ascending=False)
country_singedin_sorted_restindex = country_singedin_sorted.reset_index()
for i, row in country_singedin_sorted_restindex.iterrows(): #iterrows means take to for loop
    if i == 0:
        print("{} ({} contracts)".format(row['COUNTRY'],row['CONTRCNT']))

#5 How many unique City has customer least 1
print("Unique cities with at least one customer:")
unique_city = df[(df['CONTRCNT']>0)]
unique_city_cnt = len(unique_city['CITY'].unique())
print(unique_city_cnt)