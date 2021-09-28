import pandas as pd
import csv
import collections

df = pd.read_csv("country.csv")

#1 Get No. of Customer
customer_num = len(df['ID'].unique())
print("No. of Customer:",customer_num)

#2 Get No. of Customer each City (Sort by city name ASC)
#2.1 Pandas
city = df.groupby('City').ID.nunique().reset_index()
city_sorted = city.sort_values(by=['City'])
for i, row in city_sorted.iterrows():
    print("City {}: No. of Customer: {}".format(row['City'],row['ID']))
    #print(f"City {row['City']}: No. of Customer: {row['ID']}")

# for i, row in city_sorted.iterrows():
#     if i == 0:
#         print("City {}: No. of Customer: {}".format(row['City'],row['ID']))
#        #print(f"City {row['City']}: No. of Customer: {row['ID']}")

#2.2 Orignal Python
# city_dict = {}
# for i in df['City']:
#     if i in city_dict:
#         city_dict[i] += 1
#     else:
#         city_dict[i] = 1

# city_dict = sorted(city_dict.items(), key=lambda x: x[0])
# for key,value in city_dict:
#     print("City:{} No. of Customer : {}".format(key,value))


# #3 Get No. of Customer each Country (Sort by country name ASC)
# country_dict = {}
# for k in df['Country']:
#     if k in country_dict:
#         country_dict[k] += 1
#     else:
#         country_dict[k] = 1

# country_dict = sorted(country_dict.items(), key=lambda x: x[0])
# for key,value in country_dict:
#     print("Country:{} No. of Customer : {}".format(key,value))

# #4 Which country has largest customers contract singed in and How many customers contract singed in
# country_singedin = df[['Country','Contrcnt']].groupby('Country').sum().reset_index()
# country_singedin2 = df['Contrcnt'].max()
# country_singedin3 = country_singedin[country_singedin['Contrcnt'] == country_singedin2]
# country_singedin_sorted = country_singedin3.sort_values(by=['Country'], ascending=False)
# for _, row in country_singedin_sorted.iterrows():
#     print("Country {}: No. of Contrcnt: {}".format(row['Country'],row['Contrcnt']))

#5 How many unique City has customer for 1



