def check(word,subword):
    a = word
    b = word[::-1]
    found = False
    for i in range (len(word)-len(subword)+1):
        if a[i:len(subword)+i] == subword:
            found = True
        elif b[i:len(subword)+i] == subword:
            found = True
    return found



print(check('gdfgdscard','ca'))
print(check('afafaocf','ca'))
