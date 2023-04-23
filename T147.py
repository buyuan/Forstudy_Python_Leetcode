from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #插叙,一个一个插入新链表
        dummy = ListNode(-1)
        while head:
            temp = head.next
            cur = dummy
            #从前往后遍历，因为没法从后往前,所以，从前往后，找到一个比head.val大的，就交换
            #用cur.next, 因为要用cur接住next
            while cur.next and cur.next.val<=head.val:
                cur = cur.next
            #当前cur.next指向的节点值比head大，所以，应该吧head换过来
            head.next = cur.next
            cur.next = head
            #然后从循环开始的下一个节点开始下次循环
            head = temp
        return dummy.next





'''
147. Insertion Sort List
Medium
Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

The steps of the insertion sort algorithm:

Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
It repeats until no input elements remain.
The following is a graphical example of the insertion sort algorithm. The partially sorted list (black) initially contains only the first element in the list. One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.
Example 1:
Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Constraints:

The number of nodes in the list is in the range [1, 5000].
-5000 <= Node.val <= 5000
'''