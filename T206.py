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
    def reverseList_iter(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #迭代，保存指向后一个节点的节点，然后将前一个指向前一个
        pre = None
        cur = head
        while cur:
            #将cur的下一个节点保存
            next = cur.next
            #将cur指向前一个节点
            cur.next = pre
            #都往前走一步
            pre = cur
            cur = next
        return pre

    #recursive
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        #当前节点后面的在调用函数中会反转, recersed 实际是一个新的链表的表头，里面的方向是倒序的
        reversed = self.reverseList(head.next)
        #反转当前节点
        #当前节点的下一个节点（正序）指向自己（逆序）
        head.next.next = head
        head.next=None

        return reversed





'''
206. Reverse Linked List
Easy
Given the head of a singly linked list, reverse the list, and return the reversed list.
Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:
Input: head = [1,2]
Output: [2,1]
Example 3:
Input: head = []
Output: []
Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
'''