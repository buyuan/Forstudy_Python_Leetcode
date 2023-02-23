# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        #inorder: left->root->right
        #preorder: root->left->right
        #所以，preoder的第一个节点就是root，然后根据inorder，知道根的左右两个子树，然后各个子树分别调用
        if not preorder or not inorder:
            #数组已经空了
            return None
        node = TreeNode(preorder[0])
        #inorder中，index左边是左树inorder，右边是右树inorder
        #preorder中，index是右树的preorder，1～index-1是左树的preorder
        index = inorder.index(preorder[0])
        iL = inorder[:index]
        iR = inorder[index+1:]
        pL = preorder[1:index+1]
        pR = preorder[index+1:]
        node.left  =self.buildTree(pL,iL)
        node.right =self.buildTree(pR,iR)
        return node




'''
105. Construct Binary Tree from Preorder and Inorder Traversal
Medium
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]
Constraints:
1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
'''