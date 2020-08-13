def fizz(n):
    answer = [] 
    for i in range(1, n+1): 
        if i % 3 == 0 and i % 5 == 0:               
            answer.append("FizzBuzz") 
        elif i % 5 == 0: 
            answer.append("Buzz") 
        elif i % 3 == 0: 
            answer.append("Fizz") 
        else: 
            answer.append(str(i)) 
    return answer

print(fizz(15))