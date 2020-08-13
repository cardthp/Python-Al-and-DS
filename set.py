my_set = set()
limit_size = 3

while len(my_set) != limit_size:
    my_set.add(input('Enter Number: '))

for num in my_set:
    print(num)