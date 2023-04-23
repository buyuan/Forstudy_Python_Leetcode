class Solution:
    #1,recursion, 按照题目的意思，左右括号返回1 是base case
    def scoreOfParentheses(self, s: str) -> int:
        return self.score(s, 0, len(s)-1)
    def score(self,s,left,right)->int:
        #base case
        if left+1==right:return 1
        #下面看字符串是否是两种情况，一个是完全对称，一个是两组，
        #如果是完全对称，拆除外面括号，乘以2，递归，如果是两组（找到一组是完全对称），则拆分成两组分开计算
        flag = 0
        for i in range(left,right):
            #不扫描到最后一个，因为如果到最后一个还不是两组，那说明是一组对称
            if s[i]=="(":flag+=1
            elif s[i] == ")": flag -= 1
            if flag==0:
                #找到分割部分
                return self.score(s,left,i)+self.score(s,i+1,right)
        #出来了说明是对称的，里面没成功,去掉外层
        return 2*self.score(s,left+1,right-1)


'''
856. Score of Parentheses
Medium
Given a balanced parentheses string s, return the score of the string.

The score of a balanced parentheses string is based on the following rule:

"()" has score 1.
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.


Example 1:

Input: s = "()"
Output: 1
Example 2:

Input: s = "(())"
Output: 2
Example 3:

Input: s = "()()"
Output: 2


Constraints:

2 <= s.length <= 50
s consists of only '(' and ')'.
s is a balanced parentheses string.
'''