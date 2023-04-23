class Solution:
    def reverseParentheses(self, s: str) -> str:
        #存储所有左括号的坐标，遇到右括号时，翻转最后一个左括号到右括号之间的部分
        #这样的好处是还不用翻转括号
        #或者是挨个加入res，存的坐标是res中左括号的坐标
        lB = []
        for i in range(len(s)):
            if s[i] == "(":
                lB.append(i)
            elif s[i] == ")":
                index = lB.pop()
                s = s[:index] + s[index:i][::-1] + s[i:]
        return s.replace("(", "").replace(")", "")


    #下面这个方法，从最外层翻转，题目要求从最内层翻转，因此会出现不一致的结果
    def reverseParentheses_outerToInner(self, s: str) -> str:
        flag = 0
        res=""
        #不能用for，因为在循环中要操纵i，而for的i在循环以后不会被影响
        i=0
        while i<len(s):
            if s[i]=="(":
                flag+=1
                stk = []
                i+=1
                while flag > 0 and i < len(s):
                    if s[i] == ")":
                        flag -= 1
                        if flag == 0: break
                    elif s[i]=="(":
                        flag+=1
                    stk.append(s[i])
                    i += 1
                # s[i]已经进栈了，所以出来以后就要再走一个
                i += 1
                next=False
                tmp=""
                while stk:
                    cur = stk.pop()
                    if cur == ")" or cur =="(":
                        next = True
                        # 反括号反过来是正括号
                        if cur==")":tmp += "("
                        else:tmp+=")"
                        continue
                    tmp+=cur
                if next:
                    res+=self.reverseParentheses(tmp)
                else:
                    res+=tmp
            if i < len(s) and s[i]!="(" and s[i]!=")":
                res += s[i]
            # 下一次循环
            i += 1
        return res


    #下面这个方法不能处理， （asd)asd(sd)asd(asda)这种情况
    def reverseParentheses_bad(self, s: str) -> str:
        # 找到括号的坐标，然后从内到外，依次反转
        lB,rB=[],[]
        for i in range(len(s)):
            if s[i]=="(":
                lB.append(i)
            elif s[i]==")":
                rB.append(i)
        while lB and rB:
            l = lB.pop()
            r = rB.pop(0)
            s = s[:l+1]+s[l+1:r][::-1]+s[r:]
        #再处理一遍，去掉括号，上面的结果会保留括号，因为坐标是括号的坐标，不能在过程中减少括号导致坐标偏移
        s.replace("(","").replace(")","")
        return s







'''
1190. Reverse Substrings Between Each Pair of Parentheses
Medium
You are given a string s that consists of lower case English letters and brackets.

Reverse the strings in each pair of matching parentheses, starting from the innermost one.
Your result should not contain any brackets.
Example 1:
Input: s = "(abcd)"
Output: "dcba"
Example 2:
Input: s = "(u(love)i)"
Output: "iloveu"
Explanation: The substring "love" is reversed first, then the whole string is reversed.
Example 3:

Input: s = "(ed(et(oc))el)"
Output: "leetcode"
Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.


Constraints:

1 <= s.length <= 2000
s only contains lower case English characters and parentheses.
It is guaranteed that all parentheses are balanced.
'''