from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #层序遍历，节点如果在这一层，位置时i，则左子节点在其所在一层位置为2^i-1,右子节点的位置为2^i
        if not root:return 0
        que = [] #用来存节点和节点在其所在行的位置
        que.append([root,1])
        res = 1
        while que:
            #当某一层只有一个节点时，相当于从这个节点重新开始，所以左边界重新赋值1
            if len(que)==1:
                que[0][1]=1
            left = que[0][1]
            right = left
            length=len(que)
            for i in range(length):
                #这里que是当作queue用，所以每次都是取队首
                nd = que[0][0]
                right = que[0][1]
                que.pop(0)
                if nd.left:que.append([nd.left,right*2-1])
                if nd.right: que.append([nd.right, right * 2])
            res = max(res,right-left+1)
        return res


'''
662. Maximum Width of Binary Tree
Medium
Given the root of a binary tree, return the maximum width of the given tree.
The maximum width of a tree is the maximum width among all levels.
The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.
It is guaranteed that the answer will in the range of a 32-bit signed integer.
Example 1:
Input: root = [1,3,2,5,3,null,9]
Output: 4
Explanation: The maximum width exists in the third level with length 4 (5,3,null,9).
Example 2:
Input: root = [1,3,2,5,null,null,9,6,null,7]
Output: 7
Explanation: The maximum width exists in the fourth level with length 7 (6,null,null,null,null,null,7).
Example 3:
Input: root = [1,3,2,5]
Output: 2
Explanation: The maximum width exists in the second level with length 2 (3,2).
Constraints:
The number of nodes in the tree is in the range [1, 3000].
-100 <= Node.val <= 100
'''