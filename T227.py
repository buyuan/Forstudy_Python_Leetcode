class Solution:
    def calculate(self, s: str) -> int:
        stk=[]
        i=0
        # 先处理乘法除法，
        curNum=0
        minusFlag=False
        while i<len(s):
            start = i
            if s[start].isdigit():
                while i<len(s) and s[i].isdigit():
                    i+=1
                curNum = int(s[start:i])
                if minusFlag:
                    curNum = 0-curNum
                    minusFlag=False
                if i >= len(s): break
            #此时i已经指向操作符
            if s[i]=="+":
                stk.append(curNum)
            elif s[i]=="-":
                stk.append(curNum)
                minusFlag=True
            elif s[i]=="*":
                i+=1
                #中间有空格
                while s[i] == " ":
                    i += 1
                start=i
                if s[start].isdigit():
                    while i<len(s) and s[i].isdigit():
                        i += 1
                nextNum = int(s[start:i])
                # //是向下取整，所以-3/2 =-2， 因为-1.5向下是-2，所以，要变成直接截取整数部分
                # curNum //= nextNum
                curNum = int(curNum / nextNum)
            elif s[i]=="/":
                i += 1
                # 中间有空格
                while s[i] == " ":
                    i += 1
                start = i
                if s[start].isdigit():
                    while i<len(s) and s[i].isdigit():
                        i += 1
                nextNum = int(s[start:i])
                curNum //= nextNum
            i+=1
        #最后一个数字没法在while里面添加
        stk.append(curNum)
        res=0
        for item in stk:
            res+=item
        return res









'''
227. Basic Calculator II
Medium
Given a string s which represents an expression, evaluate this expression and return its value.

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().



Example 1:

Input: s = "3+2*2"
Output: 7
Example 2:

Input: s = " 3/2 "
Output: 1
Example 3:

Input: s = " 3+5 / 2 "
Output: 5


Constraints:

1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer.
'''