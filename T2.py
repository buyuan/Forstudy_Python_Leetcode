from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #这个和T445的不一样就是，head节点是个位,所以也不需要栈存节点
        #用l1作为主要链条
        dummy1 = ListNode(0,l1)
        dummy2 = ListNode(0,l2)
        while l1 and l2:
            #用来判断l1长还是l2长，以决定哪个链为主链
            l1 = l1.next
            l2 = l2.next
        headFlag = True
        if l2:
            #如果l2长，则是False，则用l2作为主链条
            headFlag = False

        # l1,l2回复原状
        l1 = dummy1.next
        l2 = dummy2.next
        addFlag=0

        while l1 and l2:
            cur = l1.val+l2.val+addFlag
            if cur>=10:
                addFlag=1
                cur-=10
            else:
                addFlag=0
            if headFlag:
                l1.val = cur
            else:
                l2.val = cur
            l1=l1.next
            l2=l2.next


        while l1:
            #l2 空
            cur = l1.val + addFlag
            if cur>=10:
                addFlag=1
                cur-=10
            else:
                addFlag=0
            l1.val = cur
            l1 =  l1.next

        while l2:
            #l1 空
            cur = l2.val + addFlag
            if cur >= 10:
                addFlag = 1
                cur -= 10
            else:
                addFlag = 0
            l2.val = cur
            l2 = l2.next
        l1 = dummy1.next
        l2 = dummy2.next
        if addFlag==1:
            # 要在最后补一个1
            lastNode = ListNode(1)
            if headFlag:
                while l1.next:
                    l1 = l1.next
                l1.next = lastNode
                return dummy1.next
            else:
                while l2.next:
                    l2 = l2.next
                l2.next = lastNode
                return dummy2.next
        else:
            if headFlag:
                return dummy1.next
            else:
                return dummy2.next


'''
2. Add Two Numbers
Medium
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.



Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''