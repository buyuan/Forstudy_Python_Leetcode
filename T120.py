class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        #从三角形的底边到定点，这样的好处是，除了底边，其他每个点的上面都有两个点，代码更简单
        #dp[i][j]表示从底边到i,j点的最小总和，
        #dp[i][j] = triangle[i][j]+min(dp[i-1][j],dp[i][j-1])
        dp = triangle
        #最底边增加一个全0的一条边，方便遍历
        newEdge = [0]*(len(triangle[len(triangle)-1])+1)
        dp.append(newEdge)
        row = len(dp)
        for r in range(row-2,-1,-1):
            for c in range(len(dp[r])):
                dp[r][c] = dp[r][c]+min(dp[r+1][c],dp[r+1][c+1])
        return dp[0][0]

'''
120. Triangle
Medium
Given a triangle array, return the minimum path sum from top to bottom.
For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.
Example 1:
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
Example 2:
Input: triangle = [[-10]]
Output: -10
Constraints:
1 <= triangle.length <= 200
triangle[0].length == 1
triangle[i].length == triangle[i - 1].length + 1
-104 <= triangle[i][j] <= 104

'''