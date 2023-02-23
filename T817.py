from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def numComponents(self, head: Optional[ListNode], nums: list[int]) -> int:
        #先将nums放在set中，然后扫描链表，找到component之后，+1， 然后找到链接的终点，再找下一个component
        st = set()
        for i in nums:
            st.add(i)
        #in case there is only one node in the linked list
        if not head.next:
            if head.val in st:
                return 1
            else:
                return 0
        ans = 0
        while head:
            if head.val in st:
                ans+=1
                #找到不在nums里面的节点
                while head.next and head.next.val in st:
                    head = head.next
            head = head.next
        return ans


'''
817. Linked List Components
Medium
870
2K
company
Uber
company
Google
You are given the head of a linked list containing unique integer values and an integer array nums that is a subset of the linked list values.
Return the number of connected components in nums where two values are connected if they appear consecutively in the linked list.
Example 1:
Input: head = [0,1,2,3], nums = [0,1,3]
Output: 2
Explanation: 0 and 1 are connected, so [0, 1] and [3] are the two connected components.
Example 2:


Input: head = [0,1,2,3,4], nums = [0,3,1,4]
Output: 2
Explanation: 0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the two connected components.


Constraints:

The number of nodes in the linked list is n.
1 <= n <= 104
0 <= Node.val < n
All the values Node.val are unique.
1 <= nums.length <= n
0 <= nums[i] < n
All the values of nums are unique.
'''