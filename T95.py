from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    #从1到n中，选出i个作为root，剩下的，自然，左边是左子树（都比i小），右边是右子树
    #所以，问题变成了，左边，右边有多少种形式，每一个左边或者右边，也是同样的问题，
    #所以，依次递归，一直到剩一个节点，或者没有节点
    def generateTrees(self, n: int) -> list[Optional[TreeNode]]:
        if n==0:return []
        #helper返回的是，所有树的root
        return self.helper(1,n)

    def helper(self,start,end):
        #比如，1，10的情况，需要返回None，因为后面要循环走起来，None占个位置
        if end<start:return [None]
        res = []
        for i in range(start,end+1):
            leftNdList = self.helper(start,i-1)
            rightNdList = self.helper(i+1,end)
            for l in leftNdList:
                for r in rightNdList:
                    #依次左边选一种，右边选一种，接到i的左右两边
                    root = TreeNode(i,l,r)
                    res.append(root)
        return res



'''
95. Unique Binary Search Trees II
Medium
Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.
Example 1:
Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
Example 2:
Input: n = 1
Output: [[1]]


Constraints:

1 <= n <= 8
'''