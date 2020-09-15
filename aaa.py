def maxsubarray(alist):
    if max(alist)<0:
        return max(alist)
    curr_sum, max_sum = 0, 0
    for i in alist:
        curr_sum = max(0, curr_sum + i)
        max_sum = max(curr_sum, max_sum)
    return max_sum   

print(maxsubarray([-2,1,-3,4,-1,2,1,-5,4]))

print(maxsubarray([-2,1,-3,4]))

print(maxsubarray([-2,1]))


#Input: [-2,1,-3,4,-1,2,1,-5,4], 1 4 2 1 8
#Output: 6
#Explanation: [4,-1,2,1] has the largest sum = 6.