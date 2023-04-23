from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal_nonRecur(self, root: Optional[TreeNode]) -> list[int]:
        #这里用栈做，左子树一直入站，什么时候才能访问这个节点呢，首先，如果这个节点是叶子节点，可以访问
        #如果这个节点是根节点（右子树已经访问），则可以访问
        ans=[]
        stk=[]
        pre=None
        while root or len(stk)>0:
            while root:
                stk.append(root)
                root=root.left
            if len(stk)>0:
                root = stk.pop()
                if not root.right or pre==root.right:
                    #是根节点（左右子树都为空）或者右子树已经访问过（pre==cur.right)
                    ans.append(root.val)
                    pre=root#当前节点记录为上一个节点
                    #跳过下次循环，入栈左子树的情况，因为在栈中的节点左子树都已经入栈
                    root=None
                else:
                    #不访问该节点
                    stk.append(root)
                    #进入该节点右子树，然后以此为根，走下一个循环
                    root =root.right
        return ans

    def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        # left,right,root
        # recursive
        ans = []
        if not root:
            return ans
        self.helper(root.left, ans)
        self.helper(root.right, ans)
        ans.append(root.val)
        return ans

    def helper(self, root, ans):
        if not root:
            return
        self.helper(root.left, ans)
        self.helper(root.right, ans)
        ans.append(root.val)


'''
145. Binary Tree Postorder Traversal
Easy
Given the root of a binary tree, return the postorder traversal of its nodes' values.
Example 1:
Input: root = [1,null,2,3]
Output: [3,2,1]
Example 2:
Input: root = []
Output: []
Example 3:
Input: root = [1]
Output: [1]
Constraints:
The number of the nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
'''