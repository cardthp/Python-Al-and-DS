def gcd(a,b):
    while b > 0:
        a, b = b, a % b
    return a
    
def lcm(a, b):
    return int(a * b / gcd(a, b))

#a = int(input("Please input first number : "))
#b = int(input("Please input second number : "))

print(gcd(10,2))
print(lcm(10,2))