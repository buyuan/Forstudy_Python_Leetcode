# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, nodes: list[TreeNode]) -> TreeNode:
        self.st = set()
        for nd in nodes:
            self.st.add(nd)
        return self.findLCA(root)

    def findLCA(self,nd):
        #没有找到，找到最低点了，就返回none
        if not nd:
            return None
        #找到了一个（其实就是第一次找到，就是这条线的第一个其实）
        if self.st.__contains__(nd):
            return nd
        left = self.findLCA(nd.left)
        right = self.findLCA(nd.right)

        #如果左右都有，说明当前这个就是（因为是从上到下找，所以第一个就是最高的那个（就是在往下就分开了，不可能有了）
        if left and right:
            return nd
        #如果只有一边有，那么说明单独那条线存在一个更低的，不可能同时都没有
        if not left:
            return right
        else:
            return left
'''
1676. Lowest Common Ancestor of a Binary Tree IV
Medium
Given the root of a binary tree and an array of TreeNode objects nodes, return the lowest common ancestor (LCA) of all the nodes in nodes. All the nodes will exist in the tree, and all values of the tree's nodes are unique.

Extending the definition of LCA on Wikipedia: "The lowest common ancestor of n nodes p1, p2, ..., pn in a binary tree T is the lowest node that has every pi as a descendant (where we allow a node to be a descendant of itself) for every valid i". A descendant of a node x is a node y that is on the path from node x to some leaf node.

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [4,7]
Output: 2
Explanation: The lowest common ancestor of nodes 4 and 7 is node 2.
Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [1]
Output: 1
Explanation: The lowest common ancestor of a single node is the node itself.

Example 3:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [7,6,2,4]
Output: 5
Explanation: The lowest common ancestor of the nodes 7, 6, 2, and 4 is node 5.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-109 <= Node.val <= 109
All Node.val are unique.
All nodes[i] will exist in the tree.
All nodes[i] are distinct.'''