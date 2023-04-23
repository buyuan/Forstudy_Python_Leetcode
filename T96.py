class Solution:
    def numTrees(self, n: int) -> int:
        #卡塔兰数列
        #C0=1, Cn+1 = ECiCn-i (n>=0, i from 0 to n)
        dp=[0]*(n+1)
        dp[0],dp[1] = 1,1
        for i in range(2,n+1):
            for j in range(i):
                dp[i] += dp[j]*dp[i-j-1]
        return dp[n]


'''
96. Unique Binary Search Trees
Medium
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.
Example 1:
Input: n = 3
Output: 5
Example 2:
Input: n = 1
Output: 1
Constraints:
1 <= n <= 19
'''