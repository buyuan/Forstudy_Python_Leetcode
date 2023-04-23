from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal_nonRecur(self, root: Optional[TreeNode]) -> list[int]:
        ans=[]
        stk=[]
        while root or len(stk)>0:
            while root:
                ans.append(root.val)
                stk.append(root)
                root = root.left
            if len(stk)>0:
                root = stk.pop()
                root = root.right
        return ans

    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        #根, 左，右，
        ans=[]
        self.helper(root,ans)
        return ans

    def helper(self, root, ans):
        if not root:
            return
        ans.append(root.val)
        self.helper(root.left,ans)
        self.helper(root.right, ans)



'''
144. Binary Tree Preorder Traversal
Easy
Given the root of a binary tree, return the preorder traversal of its nodes' values.
Example 1:
Input: root = [1,null,2,3]
Output: [1,2,3]
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