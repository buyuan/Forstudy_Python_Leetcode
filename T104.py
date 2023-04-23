from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #用BFS遍历到最后一层
        ans = 0
        if root:ans+=1
        else:return ans
        que=[]
        que.append([root])
        while len(que)>0:
            cur = que.pop(0)
            temp = []
            for node in cur:
                if node.left:temp.append(node.left)
                if node.right: temp.append(node.right)
            if temp:
                ans+=1
                que.append(temp)
        return ans




'''
104. Maximum Depth of Binary Tree
Easy
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2


Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
'''