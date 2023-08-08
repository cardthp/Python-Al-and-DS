# 217. Contains Duplicate (Easy)
# Input: nums = [1,2,3,1] Output: true
# Input: nums = [1,2,3,4] Output: false

def containsDuplicate(nums):
    if len(nums) != len(set(nums)):
        return True
    else:
        return False
    
print(containsDuplicate([1,2,3,1]))