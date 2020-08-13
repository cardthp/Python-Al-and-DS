from datetime import datetime

date_str1 = '6 June 2018'
date_str2 = '6/6/18'
date_str3 = '06-06-2018'

date_dt1 = datetime.strptime(date_str1, '%d %B %Y')
date_dt2 = datetime.strptime(date_str2, '%m/%d/%y')
date_dt3 = datetime.strptime(date_str3, '%m-%d-%Y')

print(date_dt1)
print(date_dt2)
print(date_dt3)