# 540. Single Element in a Sorted Array (Medium) >> Binary Search/Two Pointer
# Input: nums = [1,1,2,3,3,4,4,8,8] Output: 2
# Input: nums = [3,3,7,7,10,11,11] Output: 10
# >> https://www.youtube.com/watch?v=HGtqdzyUJ3k
# >> เอาตัวที่ไม่ dup ใน list
# >> หลักการคือหาตัว mid เทียบดูกับตัวเองก่อนว่าตัวเองเป็น dup ไหม ถ้า dup ให้ขยับซ้าย แล้วดูว่าฝั่งซ้ายหรือฝั่งขวาที่เป็นจำนวนคี่ แล้วตัดการค้นหาไปเรื่อยๆ
def singleNonDuplicate(nums:int) -> int:
    left = 0
    right = len(nums)-1

    while left <= right:

        m = left + ((right-left)//2) #เอาด้านซ้ายมาบวกกับ subarray ที่เหลือที่ไม่โดนตัด

                # เงื่อนไขนี้เรียกว่าทำอันสุดท้ายเลยก้ได้
            # ก้อนแรก - ตัวแรกคือเช็ค out of bound ไม่ให้หลุดกรอบด้านซ้าย ตัวสองเช็คว่าข้างๆด้านซ้ายต้องไม่ตรง(ยืนยันตอนเหลือตัวสุดท้าย)
            # ก้อนสอง - ตัวแรกคือเช็ค out of bound ไม่ให้หลุดกรอบด้านขวา ตัวสองเช็คว่าข้างๆด้านขวาต้องไม่ตรง(ยืนยันตอนเหลือตัวสุดท้าย)
        if ( (m-1 < 0 or nums[m-1] != nums[m]) and (m+1 == len(nums) or nums[m+1] != nums[m]) ) :
            return nums[m]

            # leftSize คือการแบ่งเป็นซ้ายขวา ซึ่งถ้าฝั่งไหนหาร 2 ลงตัวก็ไม่นับอยู่แล้วเพราะว่ายังไงก็ dup 
            # แล้วยึดตัวซ้ายเป็นหลักไม่ให้ด้านซ้ายซ้ำกับค่า mid ให้เอาตัวนั้นเป็น leftSize
        leftSize = m-1 if nums[m-1] == nums[m] else m

            # จากนั้นเช็คค่า leftSize ว่าหาร 2 ลงไหม ถ้าไม่ลงตัวต้องตัดด้านขวาทิ้ง ถ้าลงตัวตัดซ้าย 
            # (เนื่องจาก leftSize มันยึดอยู่ทางด้านซ้ายแล้ว ทำให้ตัดสินใจได้ว่าต้องตัดซ้ายหรือตัดขวา)
        if leftSize % 2 != 0: #ถ้าไม่ลงตัวจะเข้าเงื่อนไขนี้
            right = m-1
        else:
            left = m+1
                    
print(singleNonDuplicate([1,1,2,3,3,4,4,8,8]))


# ทดสอบแบบไม่มีอธิบาย
def singleNonDuplicate2(nums:int) -> int:
    left = 0
    right = len(nums)-1

    while left <= right:
        m = left + ((right-left)//2)
    
        if ((m-1<0 or nums[m-1] != nums[m]) and (m+1==len(nums) or nums[m+1] != nums[m])):
            return nums[m]
    
        leftSize = m-1 if nums[m-1] == nums[m] else m

        if leftSize%2!=0:
            right = m - 1
        else:
            left = m +1


print(singleNonDuplicate2([3,3,7,7,10,11,11]))