# 55. Jump Game (Medium)
# Input: nums = [2,3,1,1,4] Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Input: nums = [3,2,1,0,4] Output: false
# Explanation: You will always arrive at index 3 no matter what. 
# Its maximum jump length is 0, which makes it impossible to reach the last index.
# >> https://www.youtube.com/watch?v=Yan0cv2cLy8 (Greedy algorithm)
# >> ไล่จากต้นจนจบ ว่าสามารถกระโดดไปตาม array ได้ไหม วิธีลัดคือไล่จากท้ายมาหน้า ซึ่งจากกำหนดให้ตัวที่ถอยหลังมาเป็น goal ถ้าหากได้ goal เป็น 0 จะเปรียบเสมือนถอยมาสำเร็จ

def canJump(nums):
    goal = len(nums)-1 #จำนวน array

    for i in range(len(nums)-1,-1,-1):
        if nums[i]+i >= goal: #ทำเพื่อตัดออกทีละตัวจากนั้นให้ตัวนั้นเป็น goal เลย
            goal = i

    return True if goal == 0 else False

print(canJump([2,3,1,1,4]))
print(canJump([3,2,1,0,4]))

# init goal4
# i4 goal4
# i3 goal1
# i2 goal2
# i1 goal1
# i0 goal0