class Solution:
    def minTotalDistance(self, grid: list[list[int]]) -> int:
        #这是一个数学问题，举例 一维的时候， 1000100#01000010000， 最短的举例其实是中间#的位置
        #所以是第一个和倒数第一个，第二个和倒数第二个的距离之和。
        #对于二维，则是两个1纬相加，分别是x，y两个轴
        #具体如何证明，我也不知道
        row,col = [],[]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    row.append(i)
                    col.append(j)
        row.sort()
        col.sort()
        ans = 0
        l, r = 0, len(row) - 1
        while l < r:
            ans += row[r] - row[l] + col[r] - col[l]
            r -= 1
            l += 1
        return ans

'''
296. Best Meeting Point
Hard
Given an m x n binary grid grid where each 1 marks the home of one friend, return the minimal total travel distance.
The total travel distance is the sum of the distances between the houses of the friends and the meeting point.
The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.
Example 1:
Input: grid = [[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]
Output: 6
Explanation: Given three friends living at (0,0), (0,4), and (2,2).
The point (0,2) is an ideal meeting point, as the total travel distance of 2 + 2 + 2 = 6 is minimal.
So return 6.
Example 2:
Input: grid = [[1,1]]
Output: 1
Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 200
grid[i][j] is either 0 or 1.
There will be at least two friends in the grid.
'''