# 15. 3Sum (Medium)
# Input: nums = [-1,0,1,2,-1,-4] Output: [[-1,-1,2],[-1,0,1]] Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# >> https://www.youtube.com/watch?v=jzZsG8n2R9A
# >> หลักการคล้ายๆ Container With Most Water แต่ว่าจะยึดค่าแรกเป็นหลักแล้วไปไล่สองตัวซ้ายกับขวาค่อยๆไล่เข้าหากัน

def threeSum(nums):
    res = []
    nums.sort()

    for i,value in enumerate(nums):
        if i > 0 and value == nums[i-1]: #เช็คกรณีค่าเท่ากันเช่น 1/1 หรือ -1/-1 ค่าที่ได้จะซ้ำเดิม (List จะซ้ำ โจทย์คือห้ามซ้ำ)
            continue

        left = i+1
        right = len(nums)-1

        while left<right:
            CurrentSum = value + nums[left]+nums[right]
            if CurrentSum > 0:
                right-=1
            elif CurrentSum < 0:
                left+=1
            else:
                res.append([value,nums[left],nums[right]])
                left+=1 #เพื่อทำการหาค่าต่อว่ายังสามารถทำได้อีกไหม เพื่อไม่ต้องการค่าซ้ำ
                while nums[left] == nums[left-1] and left<right: #เช็คซ้ำอีกครั้งเพื่อให้ List ไม่ซ้ำ (right ไม่ต้องทำเพราะวนไปเช็คว่าถ้ามากกว่า 0 ก็ -1)
                    left+=1
    return print(res)

threeSum([-1,0,1,2,-1,-4])