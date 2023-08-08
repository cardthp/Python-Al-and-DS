# 104. Maximum Depth of Binary Tree (Easy)
# Input: root = [3,9,20,null,null,15,7] Output: 3
# >> ไม่สามารถรันในนี้ได้เนื่องจากใน leetcode มี class ที่ไว้เก็บ left right

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))


tree_data = [3, 9, 20, '', '', 15, 7]


