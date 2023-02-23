# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #用栈存一下节点，然后从头遍历栈和list，看是否一直相等
        dummyHead = ListNode(-1)
        dummyHead.next = head
        stk = []
        while head:
            stk.append(head)
            head = head.next
        head = dummyHead.next
        while head:
            if head.val!=stk.pop().val:
                return False
            head=head.next
        return True


'''
234. Palindrome Linked List
Easy
Given the head of a singly linked list, return true if it is a
palindrome
 or false otherwise.



Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false


Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9


Follow up: Could you do it in O(n) time and O(1) space?
'''