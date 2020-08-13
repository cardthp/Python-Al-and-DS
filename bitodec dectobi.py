def biTodec(alist): #2 -> 10
    return int("".join(str(i) for i in alist),2)
    # int('101',2) 

print(biTodec([1, 0, 1]))



def decTobi(num): #10 -> 2
    if num > 1: 
        decTobi(num // 2) 
    print(num % 2, end = '') 

decTobi(5)