## """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        #NestedInteger理解为一个list或者一个抱住数字的东西，每当一个【，放入一个list，当遇到】，弹出一个list，组成新的list然后再放回去
        if not s:return NestedInteger()
        if s[0]!='[':
            #只有一个数字,没有括号
            return NestedInteger(int(s))
        stk = []
        stk.append(NestedInteger())
        i=1
        isNeg = False
        while i<len(s)-1:
            #最后一个是]所以不用跑完
            if s[i]=="-":
                isNeg=True
                i+=1
            elif s[i].isdigit():
                num = int(s[i])
                #读取完这串数字
                while i<len(s)-1 and s[i+1].isdigit():
                    num=num*10+int(s[i+1])
                    i+=1
                if isNeg:
                    num = -num
                    isNeg = False
                tp = NestedInteger(num)
                #放入上一个【对应的那个对象
                stk[-1].add(tp)
                i += 1
            elif s[i]==']':
                #需要把上一个代表【的list创建出来了,即，创建出一个list，放进前一个list中
                stk[-2].add(stk.pop())
                i+=1
            elif s[i]=='[':
                #一个新的list
                stk.append(NestedInteger())
                i+=1
            else:
                i += 1
        return stk[-1]




'''
385. Mini Parser
Medium
Given a string s represents the serialization of a nested list, implement a parser to deserialize it and return the deserialized NestedInteger.

Each element is either an integer or a list whose elements may also be integers or other lists.



Example 1:

Input: s = "324"
Output: 324
Explanation: You should return a NestedInteger object which contains a single integer 324.
Example 2:

Input: s = "[123,[456,[789]]]"
Output: [123,[456,[789]]]
Explanation: Return a NestedInteger object containing a nested list with 2 elements:
1. An integer containing value 123.
2. A nested list containing two elements:
    i.  An integer containing value 456.
    ii. A nested list with one element:
         a. An integer containing value 789


Constraints:

1 <= s.length <= 5 * 104
s consists of digits, square brackets "[]", negative sign '-', and commas ','.
s is the serialization of valid NestedInteger.
All the values in the input are in the range [-106, 106].
'''