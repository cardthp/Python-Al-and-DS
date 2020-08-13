def changetime(a):
    timee = a.split(":")
    if a[-2:] == "PM":
        if timee[0] != "12":
            timee[0] = str(int(timee[0])+12)
    else:
        if timee[0] == "12":
            timee[0] = "00"
    timee2 = ":".join(timee)
    return timee2[:-2]

test = changetime("08:10:30PM")
print(test)
