class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        #还是62dp的思路 dp[i][j] = dp[i-1][j]+dp[i][j-1],但是如果某一个是1，则dp数组中这个取值为0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[1 for i in range(n) ]for j in range(m)]
        #第一行第一列处理，如果遇到石头，后面都是0
        for j in range(n):
            if obstacleGrid[0][j]:
                while j<n:
                    dp[0][j]=0
                    j+=1
                break
        for i in range(m):
            if obstacleGrid[i][0]:
                while i<m:
                    dp[i][0]=0
                    i+=1
                break
        #开始遍历，如果上或者左有石头，都是0，因为不可能到那一点
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i - 1][j]:
                    dp[i - 1][j] = 0
                if obstacleGrid[i][j-1]:
                    dp[i][j - 1]=0
                dp[i][j] = dp[i - 1][j]+dp[i][j - 1]
                if obstacleGrid[i][j]:
                    dp[i][j]=0
        if obstacleGrid[m-1][n-1]:
            dp[m - 1][n - 1]=0
        return dp[m-1][n-1]

'''
63. Unique Paths II
Medium
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.
Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
The testcases are generated so that the answer will be less than or equal to 2 * 109.
Example 1:
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
Example 2:
Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
Constraints:
m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] is 0 or 1.
'''