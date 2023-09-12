# 232. Implement Queue using Stacks
# >> https://www.youtube.com/watch?v=nPvjcQBplH4
# >> ใช้ Stacks เป็น AL หลัก ทำให้เวลาเอาเข้าออกต้องใช้ด้านเดียวกัน
# >> โจทย์กำหนดให้เข้าด้านซ้าย

class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
            #วิธีการคือจากที่สร้าง stack 2 กล่อง โดยมี a เก็บลงไปที่ s1 ก่อนจากนั้นหากจะใส่ b เพิ่มเข้ามาต้อง peek เอา a ออกจาก s1 ไปเก็บที่ s2
        while self.s1: #while s1 is not empty (s1 ไม่ว่าง/มีค่า) ให้เอา s1 ไปใส่ใน s2
            self.s2.append(self.s1.pop())

        self.s1.append(x)

        while self.s2: #while s2 is not empty (s2 ไม่ว่าง/มีค่า) ให้เอา s2 ไปใส่ใน s1
            self.s1.append(self.s2.pop())

    def pop(self) -> int:
            #remove element front of queqe and return that element
        return self.s1.pop()

    def peek(self) -> int:
            #get front of element
        return self.s1[-1] #the last element of the array

    def empty(self) -> bool:
        return not self.s1


# Explanation
# MyQueue myQueue = new MyQueue();
# myQueue.push(1); // queue is: [1]
# myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
# myQueue.peek(); // return 1
# myQueue.pop(); // return 1, queue is [2]
# myQueue.empty(); // return false