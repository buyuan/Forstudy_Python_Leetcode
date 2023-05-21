from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        #BFS
        width,height = len(grid[0]),len(grid)
        visited = [[0]*width for i in range(height)]
        que = deque()
        res = 0
        def find_related_1(curPoint, visited, grid):
            width, height = len(grid[0]), len(grid)
            ans = []
            x, y = curPoint
            # 上
            if x - 1 >= 0 and grid[x-1][y] == 1 and not visited[x-1][y]:
                ans.append([x-1, y])
            # 左
            if y - 1 >= 0 and grid[x][y-1] == 1 and not visited[x][y-1]:
                ans.append([x, y-1])
            # 下
            if x + 1 <= height - 1 and grid[x+1][y] == 1 and not visited[x+1][y]:
                ans.append([x+1, y ])
            # 右
            if y + 1 <= width - 1 and grid[x][y+1] == 1 and not visited[x][y+1]:
                ans.append([x, y+1])
            return ans
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 0:continue
                if visited[i][j]:continue
                que.append([i,j])
                curRes=0
                while que:
                    curPoint = que.popleft()
                    #查看上下左右是否有相连的1
                    x, y = curPoint
                    if visited[x][y]:continue
                    curRes+=1
                    visited[x][y] = 1
                    valid_points = find_related_1(curPoint, visited,grid)
                    if valid_points:
                        que.extend(valid_points)
                res = max(res,curRes)
        return res




'''
695. Max Area of Island
Medium
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.



Example 1:


Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
'''