# 704. Binary Search (Easy)
# Input: nums = [-1,0,3,5,9,12], target = 9 Output: 4
# Explanation: 9 exists in nums and its index is 4
# >> หา index ไล่หา โดยแบ่งครึ่งถ้าฝั่งไหนไม่ใช่ก็จะตัดฝั่งนั้นทิ้งไปเลย
# >> วิธีแรกยังยังไงก็ต้อง sort ก่อน

def search(nums: int, target: int) -> int:
    left = 0
    right = len(nums)-1
    mid = 0

    while left <= right:
        #mid = (left+right)//2
        mid = left + ((right-left)//2)

        if nums[mid] < target:
            left = mid+1
        elif nums[mid] > target:
            right = mid-1
        else:
            return mid
    return -1

print(search([-1,0,3,5,9,12],9))


# Search แบบหาตัวที่มากที่สุด
def largest(arr):
     
    maxvalue = arr[0]
 
    for i in range(1, len(arr)):
        if arr[i] > maxvalue:
            maxvalue = arr[i]
 
    return maxvalue

print(largest([8, 10, 1000, 1, 200, 400, 500, 3, 1]))