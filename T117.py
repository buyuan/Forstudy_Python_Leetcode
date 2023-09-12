
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: Node) -> Node:
        #一层一层的遍历，遍历当前层，就把下面一层连起来
        cur = root
        #下一层第一个节点
        head=None
        #用来连接右面节点那个节点，可以理解为最右边的，没有确定next是什么的那个节点
        connector=None
        
        while cur:
            #一层的处理
            while cur:
                if cur.left:
                    #发现了起点
                    if not head:
                        head=cur.left
                        connector=cur.left
                    else:
                        connector.next=cur.left
                        connector = cur.left
                if cur.right:
                    #发现了起点
                    if not head:
                        head=cur.right
                        connector=cur.right
                    else:
                        connector.next=cur.right
                        connector = cur.right
                #cur如果有next，是因为上一层处理过，如果没有，说明是第一层或者到头了
                cur=cur.next
            #一层处理完之后，下一层
            cur=head
            head=None
            connector=None

        return root


'''
117. Populating Next Right Pointers in Each Node II
Medium
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Example 1:


Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
Example 2:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 6000].
-100 <= Node.val <= 100
 

Follow-up:

You may only use constant extra space.
The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.'''