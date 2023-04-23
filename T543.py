from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        #用来记录某个节点的最大深度，减少重复迭代
        self.mp={}
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #当前节点的直径，左子节点直径，右子节点直径的最大者,
        #直径就是左边深度加上右边深度，深度就是该节点到叶子的最大边数量
        if not root:return 0
        ans = self.getHeight(root.left) + self.getHeight(root.right)
        return max(ans,max(self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right)))

    def getHeight(self, node)->int:
        if not node:return 0
        if self.mp.__contains__(node):return self.mp[node]
        height = 1+max(self.getHeight(node.left),self.getHeight(node.right))
        self.mp[node]=height
        return height



'''
543. Diameter of Binary Tree
Easy
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Example 1:


Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1


Constraints:

The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100
'''