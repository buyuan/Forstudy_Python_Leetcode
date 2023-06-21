class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
       #dp， if text1[i] = text2[j], dp[i][j] = dp[i-1][j-1]+1, else: DP[i][j] = max(DP[i - 1][j], DP[i][j - 1])
        #dp[i][j]是指，text1，在i，text2在j，这两段有的最长共有子序列

        #+1是因为，遇到第一个字符，也要有i-1,j-1的计算，为了符合公式，所以加一个
        n,m = len(text1),len(text2)
        #注意，下面是坐标i取值范围1～n,j,1~m，所以，行是m行，列是n列
        dp = [[0]*(m+1)for i in range(n+1)]
        #循环是用的dp的index
        for i in range(1,n+1):
            for j in range(1,m+1):
                #注意是dp的index还是text的indiex
                if text1[i-1]==text2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i][j-1],dp[i-1][j])
        return dp[n][m]

'''
1143. Longest Common Subsequence
Medium
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.'''