from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        #两个队列，每次里面放的是同一层的节点,或者是用一个stack，每一层是一组节点，一组一组的处理
        ans = []
        if not root:
            return ans
        q1 = []
        q2 = []
        q1.append(root)
        temp = []
        while q1 or q2:
            while q1:
                cur = q1.pop(0)
                temp.append(cur.val)
                if cur.left: q2.append(cur.left)
                if cur.right: q2.append(cur.right)
                if not q1:
                    ans.append(temp)
                    temp = []
            # q1的跑完，换到q2跑，
            while q2:
                cur = q2.pop(0)
                temp.append(cur.val)
                if cur.left: q1.append(cur.left)
                if cur.right: q1.append(cur.right)
                if not q2:
                    ans.append(temp)
                    temp = []
        return ans



'''
102. Binary Tree Level Order Traversal
Medium
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
'''