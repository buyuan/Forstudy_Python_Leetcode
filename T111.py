import sys
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.ans=sys.maxsize
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:return 0
        level=1
        #incase 只有一个节点
        if not root.left and not root.right:
            self.ans = min(level, self.ans)
            return self.ans
        self.dfs(root.left,level)
        self.dfs(root.right, level)
        return self.ans

    def dfs(self, node, level):
        if not node:return
        level += 1
        if not node.left and not node.right:
            self.ans = min(level,self.ans)
            return
        self.dfs(node.left, level)
        self.dfs(node.right, level)


'''
111. Minimum Depth of Binary Tree
Easy
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 2
Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5


Constraints:

The number of nodes in the tree is in the range [0, 105].
-1000 <= Node.val <= 1000
'''