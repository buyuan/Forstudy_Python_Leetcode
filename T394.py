class Solution:
    def decodeString(self, s: str) -> str:
        #把左括号入栈，遇到右括号就和最后一个左括号中间的字符开始处理
        #右括号处理完，左括号也处理完了
        #注意，处理的时候，因为前面是数字，而且可能是不止一位，所以要考虑完整取值
        lB=[]
        res=""
        for i in range(len(s)):
            if s[i]=="[":
                lB.append(len(res))
                res += s[i]
            elif s[i]=="]":
                index = lB.pop()
                cur = res[index+1:]
                #往前找到数字的尽头
                start,end= index-1,index
                while res[start].isdigit():
                    start-=1
                #会比实际多前走一位
                start+=1
                t = int(res[start:end])
                res=res[:start]+t*cur
            else:
                res+=s[i]
        return res
'''
394. Decode String
Medium
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.



Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"


Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
'''