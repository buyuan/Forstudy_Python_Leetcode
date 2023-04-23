class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        #维护一个单调递增栈，
        #记录某个字符在s中的最后一个位置，如果遍历时，出现，大，小排列，且，大的这个字符在后面还有，那么直接舍弃大
        #因为大放在后面可以更小
        #当遍历到一个新的字符，发现在栈中已经存在，那么这个字符可以舍弃，因为栈是一个递增栈，后面出现的相同字符，如果删掉前面的
        #要吗没影响，比如相邻的，要么变大，比如 acdc， 去掉前一个c变成adc，明显大于去掉后一个c ， acd

        #不需要再使用26位数长度的数组来标记栈中有什么字符,python 可以判断
        lastIndex = {}
        length = len(s)
        #记录每个字符最后位置
        for i in range(length):
            lastIndex[s[i]]=i
        stk=[]
        for i in range(length):
            # 当遍历到一个新的字符，发现在栈中已经存在，那么这个字符可以舍弃，因为栈是一个递增栈，后面出现的相同字符，如果删掉前面的
            # 要吗没影响，比如相邻的，要么变大，比如 acdc， 去掉前一个c变成adc，明显大于去掉后一个c ， acd
            if s[i] in stk:continue
            while stk and s[i]<stk[-1] and lastIndex[stk[-1]]>i:
                #当前字符小于于上一个字符（栈顶原色），且上一个字符在后面还会出现，则舍弃这个栈顶元素
                stk.pop()
            stk.append(s[i])
        return "".join(stk)


'''
316. Remove Duplicate Letters
Medium
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is
the smallest in lexicographical order
 among all possible results.



Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"


Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
'''