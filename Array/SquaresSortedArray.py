# 977. Squares of a Sorted Array (Easy) >> Two Pointer
# Input: nums = [-4,-1,0,3,10] Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].After sorting, it becomes [0,1,9,16,100].
# Input: nums = [-7,-3,2,3,11] Output: [4,9,9,49,121]
# >> https://www.youtube.com/watch?v=FPCZsG_AkUg
# >> เทียบซ้ายสุดกับขวาสุดสลับไปมาจนเข้ามาหาตรงกลาง
def sortedSquares(nums: int):
    left = 0
    right = len(nums)-1
    res = []

    while left <= right:
        if nums[left]*nums[left] < nums[right]*nums[right]:
            res.append(nums[right]*nums[right])
            right -= 1
        else:
            res.append(nums[left]*nums[left])
            left += 1
    
    return res[::-1]

print(sortedSquares([-4,-1,0,3,10]))
print(sortedSquares([-7,-3,2,3,11]))