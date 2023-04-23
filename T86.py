from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head
        #先找到第一个大于等于x的点，然后把后面小于x的node依次移动到这个点前面
        dummy = ListNode(-1,head)
        pre,cur = dummy,head
        while cur and cur.val<x:
            pre=pre.next
            cur=cur.next
        pre2=pre
        while cur:
            if cur.val<x:
                #移动到pre后面
                #前一个节点指向下一个节点
                pre2.next = cur.next
                #cur下一个节点指向pre的下一个节点
                cur.next =pre.next
                #pre指向cur
                pre.next = cur
                #pre向前移动,我没明白为什么pre要向前移动，需求里没体现出来，但是测试case看要移动
                pre =cur
                #cur移动到原本的下一个节点
                cur = pre2.next
            else:
                cur = cur.next
                pre2=pre2.next
        return dummy.next

'''
86. Partition List
Medium
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.



Example 1:


Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Example 2:

Input: head = [2,1], x = 2
Output: [1,2]


Constraints:

The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200

'''