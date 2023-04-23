from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        #分治，每次合并两条链条，把后半部分合并到前半部分，比如5个链，0，3合并，1，4合并，最后处理，0，1，2
        #0，2，合并，最后处理，0，1， 合并到0
        if not lists:return None
        length = len(lists)
        while length>1:
            k = (length+1)//2
            for i in range(length//2):
                lists[i] = self.mergeTwo(lists[i],lists[i+k])
            length=k
        return lists[0]

    def mergeTwo(self, head1, head2) ->Optional[ListNode] :
        dummy =ListNode(-1)
        cur = dummy
        while head1 and head2:
            if head1.val<head2.val:
                cur.next = head1
                head1=head1.next
            else:
                cur.next = head2
                head2 = head2.next
            cur=cur.next
        if head1:
            cur.next=head1
        if head2:
            cur.next=head2
        return dummy.next


    def mergeKLists_old(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        # 尝试挨个扫描链接，每次找到最小的，但是这种方法效率太低，可以考虑分治，每次都是两两合并
        dummy = ListNode(-1)
        cur = dummy
        while lists:
            curNode = lists[0]
            if not curNode:
                lists.pop(0)
                continue
            index = 0
            for i in range(len(lists)):
                if lists[i] and lists[i].val < curNode.val:
                    curNode = lists[i]
                    index = i
            if lists[index] and lists[index].next:
                lists[index] = lists[index].next
            else:
                lists.pop(index)
            cur.next = ListNode(curNode.val)
            cur = cur.next
        return dummy.next




'''
23. Merge k Sorted Lists
Hard
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.



Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []


Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
'''