from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left= None, right= None, next = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        #层序遍历
        if not root:return root
        que = []
        que.append(root)
        while que:
            length = len(que)
            while length>0:
                cur = que.pop(0)
                if length>1:
                    #最后一个之前都可以指定，最后一个不行
                    cur.next = que[0]
                if cur.left:que.append(cur.left)
                if cur.right: que.append(cur.right)
                length -= 1
        return root



'''
116. Populating Next Right Pointers in Each Node
Medium
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.



Example 1:


Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
Example 2:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 212 - 1].
-1000 <= Node.val <= 1000

'''