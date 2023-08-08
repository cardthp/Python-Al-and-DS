# 11. Container With Most Water (Medium)
# Input: height = [1,8,6,2,5,4,8,3,7] Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
#             In this case, the max area of water (blue section) the container can contain is 49.
# หาปริมาณน้ำที่มากที่สุดที่ใส่ได้ หาโดยการเริ่มจากเสาแรกเทียบเสาสุดท้าย แล้วหา area มากสุด โดยวนว่าหากเสาไหนสูงกว่า ให้ขยับเสาอีกข้างไปเรื่อยๆ

def maxArea(height):
    result = 0
    l = 0
    w = len(height)-1

    while l < w:
            #area = width*height
        area = (w-l) * min(height[w],height[l])
        result = max(result,area)      

        if height[l] < height[w]:
            l += 1
        else:
            w -= 1
    return result  

print(maxArea([1,8,6,2,5,4,8,3,7]))


# >> brust force ทำให้ใช้เวลาเกิน
# def maxArea(height):
    # result = 0
    # for l in range(len(height)):
    #     for w in range(l+1,len(height)):
    #             #area = width*height
    #         area = (w-l) * min(height[w],height[l])
    #         result = max(result,area)
    # return result