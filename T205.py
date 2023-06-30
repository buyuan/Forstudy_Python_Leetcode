class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def st(s,t):
            if len(s)!=len(t):
                return False
            #从头到尾遍历，看map关系会不会变
            mp={}
            for i in range(len(s)):
                if not mp.get(s[i]):
                    mp[s[i]]=t[i]
                else:
                    if mp[s[i]]!=t[i]:
                        return False
            return True
        return st(s,t) and st(t,s)

'''
205. Isomorphic Strings
Easy
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
 

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.'''