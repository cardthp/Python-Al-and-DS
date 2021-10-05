m = {
    "January": "1",
    "February": "2",
    "March": "3",
    "April": "4",
    "May": "5",
    "June": "6",
    "July": "7",
    "August": "8",
    "September": "9",
    "October": "10",
    "November": "11",
    "December": "12"
}

def changeformat(a):
    date1 = a.split(" ")
    date1[1] = m.get(date1[1])
    date1[0],date1[1] = date1[1],date1[0]
    date1[2] = str(int(date1[2])+543)
    date2 = "/".join(date1)
    return date2

a = input("Enter day month year :")
print(changeformat(a))

#print(changeformat("10 December 2012")) 
#รับค่า 10 december 2012 แปลงเป็น 12/10/2555