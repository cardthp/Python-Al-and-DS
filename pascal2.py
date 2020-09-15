def pascal2(row):
    if row <= 0:
        return [1]

    elif row == 1:
        return [1,1]

    elif row >= 2:
        needrow = row - 1
        lastrow = [1,1]
        for i in range (0,needrow):
            newrow = [1]
            for j in range (1,len(lastrow)):
                newrow.append(lastrow[j-1] + lastrow[j]) 
            newrow.append(1)
            lastrow = newrow
        return lastrow

print(pascal2(5))