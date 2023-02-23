# Definition for singly-linked list.
# class ListNode:
from typing import Optional


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTheMiddle(self,head: Optional[ListNode]) -> Optional[TreeNode]:
        pre =None
        slow, fast = head, head
        #快节点每次走两步，当快节点到头了，慢节点就在中间
        while fast and fast.next:
            pre=slow
            slow=slow.next
            fast=fast.next.next
        if pre:
            #断开左右两个链条
            pre.next=None
        return slow
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        #BST的性质，左子树总比根小，右子树总比根大,所以，肯定需要找到中间的节点，然后从中间拆成两段
        #递归产生两边的BST，接在根的左右两边

        #空链表
        if not head:
            return head

        mid = self.findTheMiddle(head)

        node = TreeNode(mid.val)
        #base case
        if head == mid:
            #最后只有一个节点时，可以返回,不用再找左右了
            return node
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)
        return node



'''
109. Convert Sorted List to Binary Search Tree
Medium
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a
height-balanced
 binary search tree.



Example 1:


Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
Example 2:

Input: head = []
Output: []


Constraints:

The number of nodes in head is in the range [0, 2 * 104].
-105 <= Node.val <= 105
'''