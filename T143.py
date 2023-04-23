from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList_old(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #用一个list，两头拿点
        lst=[]
        while head:
            lst.append(head)
            head = head.next
        cur = lst.pop(0)
        dummy = ListNode(-1,cur)
        ct = 0
        while lst:
            ct+=1
            #先尾，再头
            if ct%2:
                temp = lst.pop()
            else :
                temp = lst.pop(0)
            #去掉环
            temp.next = None
            cur.next = temp
            cur = cur.next
        return dummy.next

    def reorderList(self, head: Optional[ListNode]) -> None:
        #找到中点，断开链表，反转后部分链表，然后将后部分和前部分交叉插入
        slow,fast = head,head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        pre,cur =None, slow.next
        slow.next=None
        #反转nLst
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        #交叉插入,pre是反转后的头，
        fcur= head
        while fcur and pre:
            #原来的next
            next = fcur.next
            #插入后半部分链条的第一个节点
            fcur.next = pre
            pre = pre.next
            #接回来原来的next
            fcur.next.next = next
            #用来跑动的指针跑到下一个节点
            fcur = next
        #不会有后半部分比前半部分长的情况，所以，循环出来之后，nLst肯定排完了






'''
143. Reorder List
Medium
You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
Constraints:
The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
'''