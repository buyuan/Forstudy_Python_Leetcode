class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        #将push按顺序放入一个stack，如果能够和pop对应上，就pop，不行就不行了
        stk=[]
        i=0
        for num in pushed:
            stk.append(num)
            while i<len(popped) and stk and popped[i]==stk[-1]:
                stk.pop()
                i+=1
        return not stk

'''
946. Validate Stack Sequences
Medium
Given two integer arrays pushed and popped each with distinct values, return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise.

 

Example 1:

Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4),
pop() -> 4,
push(5),
pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
Example 2:

Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.
 

Constraints:

1 <= pushed.length <= 1000
0 <= pushed[i] <= 1000
All the elements of pushed are unique.
popped.length == pushed.length
popped is a permutation of pushed.'''