from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> list[list[int]]:
        #用一个栈，先右后左，一层就是一组，然后弹出，
        ans = []
        stk = []
        cur=[]
        cur.append([root])
        stk.append([root])
        while len(cur)>0:
            nodeArr = cur.pop()
            temp = []
            for node in nodeArr:
                if node.left:temp.append(node.left)
                if node.right: temp.append(node.right)
            if temp:
                stk.append(temp)
                cur.append(temp)
        while len(stk)>0:
            nodeArr = stk.pop()
            temp = []
            for node in nodeArr:
                temp.append(node.val)
            ans.append(temp)
        return ans



'''
107. Binary Tree Level Order Traversal II
Medium
Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]
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