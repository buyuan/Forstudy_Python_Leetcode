
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #   两个节点，一个指向第一个基数，另一个指向第一个偶数，然后把偶数后面的那个节点移动到奇数后面
        #   然后两个节点同时前进，又变成了，第一个节点指向奇数，第二个指向偶数，偶数后面那个指向下一个奇数
        if not head:
            return head
        dummy = ListNode(-1,head)
        pre = dummy.next
        cur = pre.next
        evenHead = pre.next
        while cur and cur.next:
            #把cur后面的节点移动到cur前面，pre后面
            pre.next = cur.next
            #cur的下一个节点指向下一个偶数节点
            cur.next = cur.next.next
            #移动过来的奇数节点的下一个指向cur
            pre.next.next = cur

            #进入下一轮移动
            pre = pre.next
            cur = cur.next
            pre.next = evenHead
        return head




'''
328. Odd Even Linked List
Medium
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.



Example 1:


Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]
Example 2:


Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]


Constraints:

The number of nodes in the linked list is in the range [0, 104].
-106 <= Node.val <= 106
'''