import copy

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:return 0
        #把每一个路径遍历出来，
        numList = []
        stk = []
        self.helper(root,numList,stk)
        ans =0
        for num in numList:
            tmp=1
            res=0
            while len(num)>0:
                res+=num.pop()*tmp
                tmp*=10
            ans+=res
        return ans

    def helper(self, node, numList, stk):
        if not node:return
        stk.append(node.val)
        if not node.left and not node.right:
            numList.append(copy.deepcopy(stk))
        length = len(stk)
        self.helper(node.left,numList,stk)
        while len(stk)>length:
            stk.pop()
        self.helper(node.right, numList, stk)

    #一边走一边算，每次把上一个值扩大10倍
    def sumNumbers_new(self, root: Optional[TreeNode]) -> int:
        if not root:return 0
        return self.helper_2(root,0)


    def helper_2(self, root, pre):
        if not root:return 0
        cur = pre*10+root.val
        if not root.left and not root.right:
            return cur
        return self.helper_2(root.left,cur)+self.helper_2(root.right, cur)

'''
129. Sum Root to Leaf Numbers
Medium
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.



Example 1:


Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:


Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.


Constraints:

The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 9
The depth of the tree will not exceed 10.
'''