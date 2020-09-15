def twoSum(nums, target):
    a = {}
    for i in range(len(nums)):
        if target - nums[i] in a:
            return [a[target - nums[i]],i]
        else:
            a[nums[i]] = i

print(twoSum([2,8,12,15], 20))