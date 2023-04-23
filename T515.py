from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> list[int]:
        #层序
        res = []
        if not root:return res
        que = []
        que.append(root)
        while que:
            length = len(que)
            levelMax = que[0].val
            while length>0:
                cur = que.pop(0)
                levelMax = max(levelMax,cur.val)
                if cur.left:que.append(cur.left)
                if cur.right: que.append(cur.right)
                length-=1
            res.append(levelMax)
        return res
'''
515. Find Largest Value in Each Tree Row
Medium
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).



Example 1:


Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]
Example 2:

Input: root = [1,2,3]
Output: [1,3]


Constraints:

The number of nodes in the tree will be in the range [0, 104].
-231 <= Node.val <= 231 - 1
'''