# 1. Two Sum (Easy)
# Input: nums = [2,7,11,15], target = 9 Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# >> use enumerate to detect array postiton

def twoSum(nums, target):
    for i,j in enumerate(nums):
        for indexx in range(i+1,len(nums)):
            if j + nums[indexx] == target:
                return [i,indexx]

print(twoSum([2,7,11,15],9))