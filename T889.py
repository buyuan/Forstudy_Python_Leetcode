from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructFromPrePost(self, preorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
        preL,preR = 0,len(preorder)-1
        postL,postR = 0,len(postorder)-1
        return self.helper(preorder,preL,preR,postorder,postL,postR)

    def helper(self, preorder, preL, preR, postorder, postL, postR):
        #规律是这样，preorder的第二个节点左子树的根，这个值，将preoder和postorder分成两棵树的两段，分别是左右子树
        if preL>preR or postL>postR:return None
        node = TreeNode(preorder[preL])
        #相等说明只有这一个节点了
        if preL==preR:return node
        leftRoot = preorder[preL+1]
        postSplit = postorder.index(leftRoot)
        #postSplit-postL就是左子树的长度,所以left的范围是左边界，左边界+长度
        node.left = self.helper(preorder,preL+1,preL+1+postSplit-postL,postorder,postL,postSplit)
        node.right = self.helper(preorder,preL+1+postSplit-postL+1,preR,postorder,postSplit+1,postR)
        return node


'''
889. Construct Binary Tree from Preorder and Postorder Traversal
Medium
Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values and postorder is the postorder traversal of the same tree, reconstruct and return the binary tree.

If there exist multiple answers, you can return any of them.



Example 1:


Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]
Example 2:

Input: preorder = [1], postorder = [1]
Output: [1]


Constraints:

1 <= preorder.length <= 30
1 <= preorder[i] <= preorder.length
All the values of preorder are unique.
postorder.length == preorder.length
1 <= postorder[i] <= postorder.length
All the values of postorder are unique.
It is guaranteed that preorder and postorder are the preorder traversal and postorder traversal of the same binary tree.
'''