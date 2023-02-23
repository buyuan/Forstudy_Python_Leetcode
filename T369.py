# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#题目的意思是链表是一个数字，从左到右的各个位数，现在要做+1的计算
#比如，1，2，3 就是123， 要做的就是输出1，2，4，  比如9，9，9， 输出1，0，0，0
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        #考虑先把各个节点入栈，然后开始+1，以及进位
        node = []
        #保留好头的指针
        dummy = ListNode(-1,head)
        while head:
            node.append(head)
            head = head.next

        digit=1
        while len(node)>0:
            curNode = node.pop()
            curVal = curNode.val+digit
            if curVal==10:
                curNode.val=0
                digit=1
            else:
                curNode.val = curVal
                digit = 0
                break
        if digit==1:
            #进位了，要新增一个节点
            return ListNode(1,dummy.next)

        return dummy.next






'''
369. Plus One Linked List
Medium
Given a non-negative integer represented as a linked list of digits, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list.



Example 1:

Input: head = [1,2,3]
Output: [1,2,4]
Example 2:

Input: head = [0]
Output: [1]


Constraints:

The number of nodes in the linked list is in the range [1, 100].
0 <= Node.val <= 9
The number represented by the linked list does not contain leading zeros except for the zero itself.
'''