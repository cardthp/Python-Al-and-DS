import random
queue = []
people = ['A','B','C']
en_number = 1
for i in range (len(people)):
    someone = random.choice(people)
    print("Q {} : {}".format(en_number,someone))
    people.remove(someone)
    queue.append(someone)
    en_number += 1

qu_number = 1
for i in range (len(queue)):
    print("Q Call {} : {}".format(qu_number,queue.pop(0)))
    qu_number += 1