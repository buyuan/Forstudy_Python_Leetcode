from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            #空或者只有一个节点
            return head
        # 把最后k个节点拆下来，反转，然后接上头节点
        dummy = ListNode(-1, head)
        len = 0
        while head:
            head = head.next
            len += 1
        head = dummy.next
        # 有可能k超过len，转回来了
        k = k % len
        for i in range(len - k - 1):
            head = head.next
        cur = head.next
        #如果cur为空，说明cur就是最后一个空节点，那么就不用移动链表
        if not cur:
            return dummy.next
        head.next = None
        res = cur
        while cur.next:
            cur = cur.next
        cur.next = dummy.next
        return res

'''
61. Rotate List
Medium
Given the head of a linked list, rotate the list to the right by k places.
Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]
Constraints:
The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
'''