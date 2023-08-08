# 53. Maximum Subarray (Medium)
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4] Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# >> Kadane's Algorithm https://www.youtube.com/watch?v=Id_hZTV7_IA
# >> หลักการเดียวกับ BestTimetoBuyandSellStock คือตั้ง variable global ขึ้นมาก่อน แล้วเทียบหาตัวมาก ไม่ใช่ก้ตัดทิ้ง

def maxSubArray(nums):
    currentmaxarray = nums[0]
    overallmaxarray = nums[0]
    for i in range (1,len(nums)):
            #check each array of currentmaxarray to idenify that max value and if currentmaxarray is more than overallmaxarray change to it 
        currentmaxarray = max(nums[i], currentmaxarray + nums[i])
        overallmaxarray = max(overallmaxarray, currentmaxarray)

    return overallmaxarray

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

