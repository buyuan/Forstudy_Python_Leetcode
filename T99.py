import sys
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        #一个错误的思路：中序遍历放在list中，找到错乱的节点，一个是比后者大，一个是比前者小,而且是先发生比后者大的
        #因为是刚好相邻，比如，321，正确的应该是找到3，1，但是实际上会找到3，2
        #所以改成，排序val。挨个给原节点赋值
        stk = []
        cur = root
        lst = []
        lstVal=[]
        indexRight,indexleft=-1,-1

        while stk or cur:
            while cur:
                stk.append(cur)
                cur = cur.left
            cur = stk.pop()
            lst.append(cur)
            lstVal.append(cur.val)
            cur = cur.right
        lstVal.sort()
        for i in range(len(lst)):
            lst[i].val = lstVal[i]








'''
99. Recover Binary Search Tree
Medium
You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.
Example 1:
Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.
Example 2:
Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.
Constraints:
The number of nodes in the tree is in the range [2, 1000].
-231 <= Node.val <= 231 - 1
'''