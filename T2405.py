class Solution:
    def partitionString(self, s: str) -> int:
        #用数组下标表示26个小写字母,出现一次重复，清空一次数组
        alpa = [0]*26
        res=0
        for i in range(len(s)):
            index = ord(s[i])-ord('a')
            #该字符出现过1次，再出现就重复了
            alpa[index]+=1
            if alpa[index]>1:
                res+=1
                #清空这个数组
                for j in range(26):
                    alpa[j]=0
                alpa[index]=1
        #最后一次因为找不到重复就出来了，所以外面要加回来
        return res+1

'''
2405. Optimal Partition of String
Medium
Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. That is, no letter appears in a single substring more than once.

Return the minimum number of substrings in such a partition.

Note that each character should belong to exactly one substring in a partition.

 

Example 1:

Input: s = "abacaba"
Output: 4
Explanation:
Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
It can be shown that 4 is the minimum number of substrings needed.
Example 2:

Input: s = "ssssss"
Output: 6
Explanation:
The only valid partition is ("s","s","s","s","s","s").
 

Constraints:

1 <= s.length <= 105
s consists of only English lowercase letters.'''