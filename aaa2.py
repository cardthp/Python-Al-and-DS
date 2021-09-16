def twoSum(nums, target):
    a = {}
    for i in range(len(nums)):
        if target - nums[i] in a:
            return [a[target - nums[i]],i]
        else:
            a[nums[i]] = i

print(twoSum([2,8,12,15], 20))

# #0
# a[2] = 0
# #1
# 20-8=12
# a[12,1]
# #2
# 20-12=8
# a[8,2]
# #3
# 20-15=5
# a[5,3]


# a[8] = 1 
# a[12] = 2
# a[15] = 3