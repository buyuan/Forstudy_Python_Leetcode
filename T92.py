# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        #思路是找到中间这段要反转的链，并记录要衔接的左右边界，然后反转链条，分别衔接到两边
        index=1
        dummy = ListNode(-1,head)
        pre = dummy
        while index<left:
            pre = pre.next
            index+=1
        #left之后就要开始反转了
        leftNode = pre
        #原本的下一个，在反转后成为最后一个
        rightEdge= leftNode.next
        cur = pre.next
        #向前移动了一个
        while index<=right and pre:
            #最后一个反转手工完成
            index+=1
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        #此时pre是最后一个节点，也是反转之后的第一个节点，cur是反转后应该接住的右边节点
        leftNode.next=pre
        rightEdge.next=cur
        return dummy.next


'''
92. Reverse Linked List II
Medium
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.



Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]


Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n
'''