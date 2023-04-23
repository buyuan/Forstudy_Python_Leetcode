from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        #就是对比一个节点的n1和左节点另一个节点n2的右节点是否相等 同时，n1的右节点和n2的左节点是否相等
        if not root:return True
        return self.isSymme(root.left,root.right)

    def isSymme(self, left: Optional[TreeNode],right: Optional[TreeNode]) -> bool:
        if not left and not right:return True
        if (left and not right) or (not left and right) or (left.val !=right.val):return False
        return self.isSymme(left.left,right.right) and self.isSymme(left.right,right.left)


'''
101. Symmetric Tree
Easy
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).



Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false


Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100

'''