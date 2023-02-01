class Solution:
    def firstUniqChar(self, s: str) -> int:
        repeatFlag = False
        for i in range(0, len(s)):
            c = s[i]
            for j in range(0, len(s)):
                if j == i:
                    continue
                if c == s[j]:
                    repeatFlag = True
                    break
            if repeatFlag:
                repeatFlag = False
                continue
            else:
                return i
        return -1

    def firstUniqChar_2(self, s: str) -> int:
        mp = {}
        for i in s:
            cur = mp.get(i,0)
            mp[i] = cur +1
        for i in range(0,len(s)):
            if mp[s[i]]==1:
                return i
        return -1


'''
387. First Unique Character in a String
Easy
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.



Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1


Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
'''