from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstFromPreorder(self, preorder: list[int]) -> Optional[TreeNode]:
        # 根左右，第一个是根，比根大的是右子树，根和右子树之间是左子树
        left = 0
        right = len(preorder) - 1
        return self.helper(preorder, left, right)

    def helper(self, preorder, left, right):
        if left > right: return None
        rootVal = preorder[left]
        root = TreeNode(rootVal)
        if left == right: return root
        splitIndex = left + 1
        found = False
        for i in range(left, right + 1):
            if preorder[i] > rootVal:
                splitIndex = i
                found = True
                break
        if found:
            root.left = self.helper(preorder, left + 1, splitIndex - 1)
            root.right = self.helper(preorder, splitIndex, right)
        else:
            root.left = self.helper(preorder, left + 1, right)
            root.right = None
        return root


'''
1008. Construct Binary Search Tree from Preorder Traversal
Medium
Given an array of integers preorder, which represents the preorder traversal of a BST (i.e., binary search tree), construct the tree and return its root.
It is guaranteed that there is always possible to find a binary search tree with the given requirements for the given test cases.
A binary search tree is a binary tree where for every node, any descendant of Node.left has a value strictly less than Node.val, and any descendant of Node.right has a value strictly greater than Node.val.
A preorder traversal of a binary tree displays the value of the node first, then traverses Node.left, then traverses Node.right.
Example 1:
Input: preorder = [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]
Example 2:
Input: preorder = [1,3]
Output: [1,null,3]
Constraints:
1 <= preorder.length <= 100
1 <= preorder[i] <= 1000
All the values of preorder are unique.
'''