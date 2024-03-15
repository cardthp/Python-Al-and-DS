# 33. Search in Rotated Sorted Array (Medium) >> Binary Search/Two Pointer
# Input: nums = [4,5,6,7,0,1,2], target = 0 Output: 4
# Input: nums = [4,5,6,7,0,1,2], target = 3 Output: -1
# >> https://www.youtube.com/watch?v=U8XENwh8Oy8
# >> หาตำแหน่งของ target ที่ต้องการ
# >> หลักการคือหาตัว mid แล้วเช็คว่าหน้าสุดมากกว่า target ไหมถ้ามากกว่าให้ตัดทิ้ง

def search(nums: int, target: int) -> int:
    left = 0
    right = len(nums)-1
    while left <= right:
        #mid = (left+right)//2
        mid = left + ((right-left)//2)
        if target == nums[mid]:
            return mid
        
        #เช็คด้านซ้ายก่อนมันมีการเรียงกันอยู่ไหม รวมถึงตัวซ้ายเท่ากับ mid ด้วย (ในทีนี้มี คือ [4 5 6]) >> L0 R6 M3 / L4 R6 M5 / L4 R5 M4
        if nums[left] <= nums[mid]:
                # เช็ค target มากกว่าตัว mid (ตัดง่ายเลย เพราะมันมากกว่าจะเทียบซ้ายทำไม >> มองตัวติดกัน) 
                # เช็ค target น้อยกว่า num ตัวซ้าย (จะได้ตัดออกไปเลยเพราะเลขที่เรียงกันมาด้านซ้ายมันเกิน >> มองตัวห่าง)
                # และทำการตัดด้านซ้ายออก
            if target > nums[mid] or target < nums[left]: 
                left = mid + 1
            else:
                right = mid - 1

        #เช็คด้านขวาก่อนมันมีการเรียงกันอยู่ไหม (ในทีนี้มี คือ [0 1 2])
        else:
                # เช็ค target น้อยกว่าตัว mid (ตัดง่ายเลย เพราะมันมากกว่าจะเทียบขวาทำไม >> มองตัวติดกัน) 
                # เช็ค target มากกว่า num ตัวขวา (จะได้ตัดออกไปเลยเพราะเลขที่เรียงกันมาด้านขวามันเกิน >> มองตัวห่าง)
                # และทำการตัดด้านขวาออก
            if target < nums[mid] or target > nums[right]:
                right = mid - 1
            else:
                left = mid + 1
    return -1

print(search([4,5,6,7,0,1,2],0))