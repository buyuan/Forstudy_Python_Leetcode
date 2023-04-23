from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #先检查后续是否有k个节点，如果有，每k个节点反转，接到主链条，然后主链遍历节点往后走k次，走到尾节点
        dummy = ListNode(-1,head)
        cur = dummy
        while head:
            node=head
            # 检查是否还剩k个节点
            '''
            if self.leftK(head,k):
                #这里有个问题，我把head丢进去，往前走了两步，出来以后，head节点丢了，所以考虑先在外面处理head，丢进去只有k个节点链条
                node = self.reverseK(head,k)
            '''
            cnt=k
            node = head
            while cnt>0 and head:
                cnt-=1
                head=head.next
            if cnt<=0:
                #说明head够长，翻转
                node = self.reverseK(node, k)
            cur.next=node
            while cur.next:
                #走到最后一个节点
                cur=cur.next
        return dummy.next
    '''
    def leftK(self,head,k):
        dummy = ListNode(-1, head)
        cur = dummy.next
        count=1
        while cur:
            if count>=k:
                return True
            cur=cur.next
            count+=1
        if count<k:
            return False
    '''

    def reverseK(self, head, k):
        #反转前k个，返回反转后的头，且让head变成第k+1个
        pre= None
        while k>0:
            k-=1
            temp = head.next
            head.next=pre
            pre=head
            head = temp
        return pre




'''
25. Reverse Nodes in k-Group
Hard
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.



Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]


Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000
'''