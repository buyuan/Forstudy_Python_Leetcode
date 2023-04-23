from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #用merge sort
        if not head or not head.next :return head
        slow,fast,pre = head,head,head
        while fast and fast.next:
            pre=slow
            slow =slow.next
            fast = fast.next.next
        #需要让两条链断开
        pre.next = None
        return self.merge(self.sortList(head),self.sortList(slow))

    def merge(self,lst1,lst2):
        #merge  返回的是一个排好序的链表的头节点，
        dummy = ListNode(-1)
        cur =dummy
        while lst1 and lst2:
            if lst1.val<lst2.val:
                cur.next = lst1
                lst1=lst1.next
            else:
                cur.next = lst2
                lst2=lst2.next
            cur =cur.next
        if lst1:
            #说明lst1大
            cur.next = lst1
        if lst2:
            cur.next = lst2
        return dummy.next


'''
148. Sort List
Medium
Given the head of a linked list, return the list after sorting it in ascending order.
Example 1:
Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:
Input: head = []
Output: []
Constraints:
The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105
'''