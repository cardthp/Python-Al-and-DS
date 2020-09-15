def countw(word):
    count = 1
    eng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in word:
        if i in eng:
            count += 1
    return count

print(countw('saveChangesInTheEditor'))
#print(countw(list('saveChangesInTheEditor')))