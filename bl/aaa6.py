from datetime import datetime

#input = '10 October 2012'

a = input("Enter day month year :")
b = datetime.strptime(a, '%d %B %Y')
print(b.strftime('%m/%d/%Y'))
