def is_slice_in_list(s,l):
    return any(s == l[i:len(s)+i] for i in range(len(l) - len(s) + 1))

A = [1,2,3,4,5,6,7,8,9,0] 

B = [4,5,6,7]
C = [7,8,9,0]
D = [4,6,7,5]


print(is_slice_in_list(B,A))
print(is_slice_in_list(C,A))
print(is_slice_in_list(D,A))