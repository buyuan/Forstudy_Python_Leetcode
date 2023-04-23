from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #用栈放节点
        dummy1 = l1
        dummy2 = l2
        lst1,lst2=[],[]
        while dummy1:
            lst1.append(dummy1)
            dummy1 = dummy1.next
        while dummy2:
            lst2.append(dummy2)
            dummy2 = dummy2.next
        addFlag = 0
        #这个flag决定用谁做主链条
        headFlag = len(lst1)>=len(lst2)
        while len(lst1)>0 and len(lst2)>0:
            node1 = lst1.pop()
            node2 = lst2.pop()
            cur = node1.val+node2.val+addFlag
            if cur >=10:
                addFlag=1
                cur = cur%10
            else:
                addFlag=0
            if headFlag:
                node1.val = cur
            else:
                node2.val = cur
        if headFlag:
            #L1长或者一样长
            # 这里就变成l1的某个位置开始+1
            while len(lst1) > 0:
                node = lst1.pop()
                cur = node.val + addFlag
                if cur >= 10:
                    addFlag = 1
                    node.val = cur % 10
                else:
                    addFlag = 0
                    node.val = cur
        else:
            # L2长
            while len(lst2) > 0:
                node = lst2.pop()
                cur = node.val + addFlag
                if cur >= 10:
                    addFlag = 1
                    node.val = cur % 10
                else:
                    addFlag = 0
                    node.val = cur
        #处理最后是否进位问题
        if addFlag==1:
            if headFlag:
                #l1
                return ListNode(1, l1)
            else:
                #l2
                return ListNode(1, l2)
        else:
            if headFlag:
                return l1
            else:
                return l2





'''
445. Add Two Numbers II
Medium
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Example 1:


Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]
Example 2:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]
Example 3:

Input: l1 = [0], l2 = [0]
Output: [0]


Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''