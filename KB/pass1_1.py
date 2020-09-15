def countString(string):
    for i in range(1, len(string)+1): #start the brute force from string length 1

        dictionary = {}
        for j in range(len(string)-i+1):  #check every combination.

            #count the substring occurrences
            try:
                dictionary[string[j:j+i]] += 1
            except:
                dictionary[string[j:j+i]] = 1

        isUnique = False #loop stops if isUnique is True
        occurrence= 0
        for key in dictionary: #iterate through the dictionary
            if dictionary[key] == 1: #check if any substring is unique
                #if found, get ready to escape from the loop and increase the occurrence
                isUnique = True
                occurrence+=1

        if isUnique: 
            return i

print(countString("aacc")) #prints (2,3)
print(countString("aatcc")) #prints (1,1)
print(countString("abaaba"))
print(countString("zyzyzyz"))
print(countString("aabbbabaaa"))