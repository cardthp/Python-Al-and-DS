# 225. Implement Stack using Queues
# >> https://www.youtube.com/watch?v=rW4vm0-DLYc
# >> ใช้ Queue เป็น AL หลัก  ทำให้เวลาเอาเข้าด้านขวาออกด้านซ้าย (เข้าออกฝั่งตรงข้าม)

from collections import deque
class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
            #เนื่องจาก Queues เป็นลักษณะที่ไม่สามารถเอาตัวลำดับที่ 1 ออกไปได้ ต้องเอา 0 ออกก่อนทำให้ต้องวนค่าทั้งหมดยกเว้นตัวที่ต้องการ input กลับเข้าไปใหม่
        for i in range(len(self.q)-1):
            self.push(self.q.popleft())
        return self.q.popleft()

    def top(self) -> int:
        return self.q[-1] #the last element of the array

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()