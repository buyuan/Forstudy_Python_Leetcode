from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        #每层节点都是从左到右加入，但是在加入val的时候，要一次正，一次反加入
        ans = []
        if not root:
            return ans
        cur = [[root]]
        l2rFlag = 1
        while cur:
            oneLevelNode = cur.pop()
            oneLevelVal = []
            tempNodeArr=[]
            for node in oneLevelNode:
                if l2rFlag%2:
                    oneLevelVal.append(node.val)
                else:
                    oneLevelVal.insert(0,node.val)
                if node.left: tempNodeArr.append(node.left)
                if node.right: tempNodeArr.append(node.right)
            ans.append(oneLevelVal)
            l2rFlag+=1
            if tempNodeArr:
                cur.append(tempNodeArr)
        return ans



'''
103. Binary Tree Zigzag Level Order Traversal
Medium
8.9K
238
company
Bloomberg
company
Amazon
company
Microsoft
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:
Input: root = [1]
Output: [[1]]
Example 3:
Input: root = []
Output: []
Constraints:
The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
'''