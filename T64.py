class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        #dp[i][j] 表示到达i，j点的最小sum
        #dp[i][j] = grid[i][j]+min(dp[i][j-1],dp[i-1][j])
        col = len(grid[0])
        row = len(grid)
        dp = [[0 for i in range(col)] for j in range(row)]
        dp[0][0]=grid[0][0]
        #初始化第一行，第一列：
        for i in range(1,col):
            dp[0][i]=grid[0][i]+dp[0][i-1]
        for j in range(1,row):
            dp[j][0]=grid[j][0]+dp[j-1][0]
        for i in range(1,row):
            for j in range(1,col):
                dp[i][j] = grid[i][j] + min(dp[i][j - 1], dp[i - 1][j])
        return dp[row-1][col-1]

'''
64. Minimum Path Sum
Medium
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.
Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12
Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 100
'''