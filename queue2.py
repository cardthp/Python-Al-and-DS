#queue = []
people = ['A','B','C']
a = 1
for i in range(len(people)):
    soe = people.pop(0)
    print("Q{}: {}".format(a,soe))
    a+=1