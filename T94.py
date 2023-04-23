# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


class Solution:
    def inorderTraversal_nonRecur(self, root: Optional[TreeNode]) -> list[int]:
        stk=[]
        ans=[]
        while root or len(stk)>0:
            while root:
                stk.append(root)
                root=root.left
            if len(stk)>0:
                root = stk.pop()
                ans.append(root.val)
                '''
                if root.right:
                    root=root.right
                else:
                    root = None
                '''
                root=root.right
        return ans

    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        #左，根，右
        ans = []
        self.helper(root,ans)
        return ans

    def helper(self, root, ans):
        if not root:
            return
        self.helper(root.left, ans)
        ans.append(root.val)
        self.helper(root.right, ans)


'''
94. Binary Tree Inorder Traversal
Easy
Given the root of a binary tree, return the inorder traversal of its nodes' values.



Example 1:


Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]


Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
'''