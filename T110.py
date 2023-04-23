from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.mp={}
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #值判断是否高度平衡（左右子树高度差小于等于1）而不是判断是否二叉搜索树
        if not root:return True
        lH,rH=0,0
        if root.left:lH=1+self.getH(root.left)
        if root.right: rH = 1 + self.getH(root.right)
        if lH>rH+1 or rH>lH+1:return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def getH(self,node):
        if not node:return 0
        if self.mp.__contains__(node):return self.mp[node]
        l,r = 0,0
        if node.left:l=1+self.getH(node.left)
        if node.right: r = 1 + self.getH(node.right)
        self.mp[node] = max(l,r)
        return max(l,r)



'''
110. Balanced Binary Tree
Easy
Given a binary tree, determine if it is
height-balanced
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true


Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
'''