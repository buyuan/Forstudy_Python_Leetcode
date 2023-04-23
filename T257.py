from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> list[str]:
        #先遍历，找到叶子，把过程中的数据加进去，用字符串存遍历结果，不要用list，以免还要考虑类似于回溯的去掉其他递归产生的影响
        ans = []
        if not root:
            return ans
        onetime_res = str(root.val)
        self.helper(root,onetime_res,ans)
        return ans

    def helper(self, node, res, ans):
        #叶子结点，加入
        if not node.left and not node.right: ans.append(res)
        if node.left:self.helper(node.left,res+"->"+str(node.left.val),ans)
        if node.right: self.helper(node.right, res + "->"+str(node.right.val), ans)


'''
257. Binary Tree Paths
Easy
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.
Example 1:
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
Example 2:
Input: root = [1]
Output: ["1"]
Constraints:

The number of nodes in the tree is in the range [1, 100].
-100 <= Node.val <= 100
'''