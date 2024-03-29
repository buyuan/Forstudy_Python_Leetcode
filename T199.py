from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        #每一层找最右的节点
        #用层序遍历
        res = []
        if not root:return res
        que = []
        que.append(root)
        while que:
            length = len(que)
            for i in range(length):
                nd = que.pop(0)
                if i ==length-1:
                    #最右面的一个节点
                    res.append(nd.val)
                if nd.left:que.append(nd.left)
                if nd.right: que.append(nd.right)
        return res


'''
199. Binary Tree Right Side View
Medium
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
Example 1:


Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
'''