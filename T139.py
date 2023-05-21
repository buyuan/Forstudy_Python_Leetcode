class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        #思路是dp， dp[i]表示前i的字符可以拆分，具体是现实，从0到i，拆成两端0，j， j+1，i，如果都能拆分，则dp[i]可以拆分
        st = set(wordDict)
        #塞一个空格，这样的话让循环跑起来，且不占位置
        s=" "+s
        dp = [False]*len(s)
        dp[0]=True
        for i in range(len(s)):
            for j in range(i):
                if dp[j] and st.__contains__(s[j+1:i+1]):
                    dp[i]=True
        return dp.pop()
'''
139. Word Break
Medium
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.



Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false


Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.

'''