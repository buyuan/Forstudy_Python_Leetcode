# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        #遍历第一颗树，然后另一个BST中查找差值的节点
        def find(aim,rt):
            if not rt:
                return False
            if rt.val==aim:
                return True
            elif rt.val <aim:
                #往右
                return find(aim,rt.right)
            elif rt.val>aim:
                #往左
                return find(aim,rt.left)

        q = deque()
        q.append(root1)
        while q:
            cur = q.pop()
            aim = target-cur.val
            if find(aim,root2):
                return True
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        return False
'''
1214. Two Sum BSTs
Medium
Given the roots of two binary search trees, root1 and root2, return true if and only if there is a node in the first tree and a node in the second tree whose values sum up to a given integer target.

 

Example 1:


Input: root1 = [2,1,4], root2 = [1,0,3], target = 5
Output: true
Explanation: 2 and 3 sum up to 5.
Example 2:


Input: root1 = [0,-10,10], root2 = [5,1,7,0,2], target = 18
Output: false
 

Constraints:

The number of nodes in each tree is in the range [1, 5000].
-109 <= Node.val, target <= 109'''