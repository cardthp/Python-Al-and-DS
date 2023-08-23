# 141. Linked List Cycle
# Input: head = [3,2,0,-4], pos = 1 Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
# >> link ต่อกันไปเรื่อยๆวนซ้ำ slow ขยับ 1 fast ขยับ 2 และสุดท้ายก็จะมาเจอกัน
# >> https://www.youtube.com/watch?v=gBTe7lFR3vc

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]):
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False