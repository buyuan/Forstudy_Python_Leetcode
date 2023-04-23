from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        #完美二叉树，每个节点都是满的。所以，把树拆分为不同的完美二叉树，如果左右两支，到头了，层数一样高，那就是完美二叉树
        #如果不一样高，左右两边分别计算，依然是左右分拆递归,完美二叉树k层， 有2^k-1个节点
        lH,rH=0,0
        lr,rr=root,root
        while lr:
            lr = lr.left
            lH+=1
        while rr:
            rr = rr.right
            rH+=1
        if lH==rH:
            #完美二叉树
            return pow(2,lH)-1
        #如果不是完美二叉树，就分拆左右两边计算
        return 1+self.countNodes(root.left)+self.countNodes(root.right)


'''
222. Count Complete Tree Nodes
Medium
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.



Example 1:


Input: root = [1,2,3,4,5,6]
Output: 6
Example 2:

Input: root = []
Output: 0
Example 3:

Input: root = [1]
Output: 1


Constraints:

The number of nodes in the tree is in the range [0, 5 * 104].
0 <= Node.val <= 5 * 104
The tree is guaranteed to be complete.
'''