# 167. Two Sum II - Input Array Is Sorted (Medium) >> Two Pointer
# Input: numbers = [2,7,11,15], target = 9 Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
# Input: numbers = [2,3,4], target = 6 Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
# >> use two pointer instead of enumerate to detect array postiton because out of memory >> เหมือนเรื่อง Container With Most Water

def twoSum(numbers, target):
    start = 0
    end = len(numbers)-1

    while start<end:
        currentSum = numbers[start] + numbers[end]

        if currentSum > target:
            end -= 1
        elif currentSum < target:
            start += 1
        else:
            return [start+1,end+1]
        
    return [] #การรันตีว่าจะออกมาเป็น List

print(twoSum([2,7,11,15],9))