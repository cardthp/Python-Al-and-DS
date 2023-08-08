# 238. Product of Array Except Self (Medium)
# Input: nums = [1,2,3,4] Output: [24,12,8,6]
# Explanation: multiply except self
# >> https://www.youtube.com/watch?v=bNvIQI2wAjk
# >> ทำโดยการไล่ prefix จากหน้าไปหลัง และไล่ postfix จากหลังไปหน้า
# >> 1.กำหนด length ของ array ให้เก็บ 1 ไปก่อน
# >> 2.ทำ prefix (ตั้งค่าเท่ากับ 1 แล้วคูณกับ input แต่ละ array ไล่จากซ้ายไปขวา 
#     โดยคูณเริ่มจากตำแหน่ง 1 เอาผล prefix เก็บไว้ใน output แล้วนำ prefix ไปคูณกับ input ตัวถัดไป)
# >> 3.ทำ postfix (ตั้งค่าเท่ากับ input array ตัวสุดท้าย แล้วคูณแต่ละ array ไล่จากขวาไปซ้าย 
#     โดยคูณเริ่มจากตำแหน่ง สุดท้าย เอาผล postfix เก็บไว้ใน output แล้วนำ postfix ไปคูณกับ input ตัวถัดไป)

def productExceptSelf(nums):
    result = [1] * len(nums)
    prefix = 1
    postfix = 1

        # (ซ้ายไปขวา) [1,1,2,6][24] << 24 จะเป็นตัวที่เกินมาเนื่องจาก array เก็บไม่พอ และให้ positon 0 เป็น prefix เลย
    for i in range(len(nums)): 
        result[i] *= prefix 
        prefix *= nums[i]

        # (ขวาไปซ้าย) [24, 12, 8, 6][4] << 4 มาจาก postfix =1 คูณ 4 
    for j in range(len(nums)-1,-1,-1):
        result[j] *= postfix
        postfix *= nums[j]
        
    return result

print(productExceptSelf([1,2,3,4]))