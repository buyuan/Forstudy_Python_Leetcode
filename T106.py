# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
        #inorder : left->root->right,  postorder: left->right->root
        self.dic={}
        for i in range(len(inorder)):
            #存一个dic,方便快速在inorder中找到根的坐标
            self.dic[inorder[i]] = i
        il,pl=0,0
        ir,pr=len(inorder)-1,len(postorder)-1
        return self.buildTree_2(il,ir,inorder,pl,pr,postorder)

    def buildTree_2(self, il,ir,inorder: list[int], pl,pr,postorder: list[int]) -> Optional[TreeNode]:
        #重载，需要index来划定新的范围（相当于新的inorder，postorder数组，用index避免拆分
        if il>ir or pl>pr:
            #到头了
            return None
        node = TreeNode(postorder[pr])
        indexRoot = self.dic[postorder[pr]]
        #左inorder的起点，终点(坐标）
        ill,ilr= il,indexRoot-1
        #右inorder的起点，终点(坐标）
        irl,irr = indexRoot+1, ir

        #左postorder的起，终坐标，plr意思是，从左边起，要先走过inorder的左子树的节点个数（indexRoot-il就是左子树节点个数）
        pll,plr = pl,pl + indexRoot - il-1
        #右 postorder，终点(坐标）
        prl,prr = pl + indexRoot - il,pr-1
        node.left =self.buildTree_2(ill,ilr,inorder,pll,plr,postorder)
        node.right =self.buildTree_2(irl,irr,inorder,prl,prr,postorder)
        return node


'''
106. Construct Binary Tree from Inorder and Postorder Traversal
Medium
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.
Example 1:
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
Example 2:
Input: inorder = [-1], postorder = [-1]
Output: [-1]
Constraints:
1 <= inorder.length <= 3000
postorder.length == inorder.length
-3000 <= inorder[i], postorder[i] <= 3000
inorder and postorder consist of unique values.
Each value of postorder also appears in inorder.
inorder is guaranteed to be the inorder traversal of the tree.
postorder is guaranteed to be the postorder traversal of the tree.
'''