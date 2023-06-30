# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        #DFS 中序遍历，左，根，右 找最小差值，BST，严格左<中<右，所以遍历出来是从小到大的顺序
        lst=[]
        def dfs(nd):
            if nd:
                dfs(nd.left)
                lst.append(nd.val)
                dfs(nd.right)
        dfs(root)
        res=100001
        for i in range(1,len(lst)):
            res = min(res,lst[i]-lst[i-1])
        return res



'''
530. Minimum Absolute Difference in BST
Easy
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

 

Example 1:


Input: root = [4,2,6,1,3]
Output: 1
Example 2:


Input: root = [1,0,48,null,null,12,49]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 104].
0 <= Node.val <= 105
 '''