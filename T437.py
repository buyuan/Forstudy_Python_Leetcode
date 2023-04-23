from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    #两个函数递归，一个是从当前节点计算有多少复合的，另外一个就是，分支开始计算
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:return 0
        return self.sumUp(root,0,targetSum)+self.pathSum(root.left,targetSum)+self.pathSum(root.right,targetSum)

    def sumUp(self, root, pre, targetSum)->int:
        if not root:return 0
        flag=0
        if pre+root.val==targetSum:
            flag=1
        return flag+self.sumUp(root.left,pre+root.val,targetSum)+self.sumUp(root.right,pre+root.val,targetSum)


        '''
        这个具体执行会有个问题，就是同一个起点会被不同的递归重复执行， 比如，爷爷节点和父节点都会导致当前节点计算
        
        #要做两个事情， 一个是这一条路继续走，另外一个是开启新的两条路
        self.helper(root.left,targetSum-root.val)
        self.helper(root.right, targetSum - root.val)

        #新的路
        self.helper(root.left, targetSum)
        self.helper(root.right, targetSum)
        '''




'''
437. Path Sum III
Medium
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.
The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).
Example 1:
Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.
Example 2:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3
Constraints:
The number of nodes in the tree is in the range [0, 1000].
-109 <= Node.val <= 109
-1000 <= targetSum <= 1000
'''