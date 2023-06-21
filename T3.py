class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #思路，当发现重复字母时，从上一次出现这个重复字符的点作为左边界重新开始滑动框
        mp={}
        l,r =0,0
        ans = 0
        while l<len(s) and r<len(s):
            if mp.get(s[r],-1)==-1:
                mp[s[r]]=r
                r+=1
            else:
                ans = max(ans,r-l)
                #l只能往后，不能往前
                l=max(l,mp.get(s[r])+1)
                mp[s[r]]=r
                r+=1
        ans = max(ans,r-l)
        return ans

        
'''
3. Longest Substring Without Repeating Characters
Medium
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''