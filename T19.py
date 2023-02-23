# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #倒数n个，可以用两个指针，一个先走n步，然后两个指针同时走， 当先走的那个指针到头时，后走的这个指针的下一个就是倒数
        #第n个，因为距离尾巴n步
        cur, pre = head,head
        for i in range(n):
            cur = cur.next
        if cur==None:
        # 说明到头了，那么此时pre就是倒数第n个
            return pre.next
        #然后同时往后移动直到到头
        while(cur.next!= None):
            cur = cur.next
            pre = pre.next
        pre.next = pre.next.next
        return head

'''
19. Remove Nth Node From End of List
Medium
Given the head of a linked list, remove the nth node from the end of the list and return its head.
Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:
Input: head = [1], n = 1
Output: []
Example 3:
Input: head = [1,2], n = 1
Output: [1]
Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
Follow up: Could you do this in one pass?
'''