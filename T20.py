class Solution:
    def isValid(self, s: str) -> bool:
        stk=[]
        for i in s:
            if stk:
                cur = stk[len(stk)-1]
                if self.compare(cur,i) :stk.pop()
                else:stk.append(i)
            else:
                stk.append(i)
        if stk:return False
        else:return True

    def compare(self,i,j):
        if i=='(':
            if j==')':
                return True
            else:return False
        if i=='[':
            if j==']':
                return True
            else:return False
        if i=='{':
            if j=='}':
                return True
            else:return False
        return False

'''
20. Valid Parentheses
Easy
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''