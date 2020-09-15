#shift to right [4, 1, 2, 3]
list1 = [1, 2, 3, 4]
a = [list1[-1]] + list1[:-1]
print(a)

#shift to left [2, 3, 4, 1]
list2 = [1, 2, 3, 4]
b = list2[1:] + [list2[0]]
print(b)

print()

def shift(key, array):
    return array[key:] + array[:key]
print (shift(1, [1, 2, 3, 4]))
print (shift(-1, [1, 2, 3, 4]))
print (shift(-3, [1,2,3,4,5,6,7]))
#[1,2,3,4,5,6,7], k = 3