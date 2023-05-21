from collections import deque


class Solution:
    def shortestBridge(self, grid: list[list[int]]) -> int:
        #先找到其中一个岛，然后四边扩展，每扩展一步，结果加1，扩展到遇到新的1（另一个岛屿）说明联通了

        #1。找到其中一个岛屿，并且改成2
        def find_island(grid,que):
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j]==1:
                        def dfs_helper(grid,x,y,que):
                            height,width = len(grid),len(grid[0])
                            if x<0 or x>=height or y<0 or y>=width or grid[x][y]==0 or grid[x][y]==2:return
                            grid[x][y] = 2
                            #把这个岛的点放入岛屿que
                            que.append([x, y])
                            dfs_helper(grid, x + 1, y, que)
                            dfs_helper(grid, x - 1, y, que)
                            dfs_helper(grid, x ,  y+1, que)
                            dfs_helper(grid, x,   y-1, que)
                        dfs_helper(grid,i,j,que)
                        return
        que = deque()
        find_island(grid,que)
        #2 开始扩展岛屿
        def find_path(que,grid):
            res=0
            #一维数组表示四个方向,下，右，上，左
            dirs = [0,1,0,-1,0]
            height, width = len(grid), len(grid[0])
            while que:
                size = len(que)
                while size>0:
                    size-=1
                    x,y = que.popleft()
                    #四个方向扩展
                    for i in range(4):
                        nx,ny = x+dirs[i],y+dirs[i+1]
                        #越界或者就是该岛屿的陆地，跳过
                        if nx<0 or nx>=height or ny<0 or ny>=width or grid[nx][ny]==2:continue
                        #扩展到另一岛屿了
                        if grid[nx][ny]==1:return res
                        grid[nx][ny]=2
                        que.append([nx,ny])
                res+=1
            return -1

        return find_path(que,grid)



'''
934. Shortest Bridge
Medium
You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.



Example 1:

Input: grid = [[0,1],[1,0]]
Output: 1
Example 2:

Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1


Constraints:

n == grid.length == grid[i].length
2 <= n <= 100
grid[i][j] is either 0 or 1.
There are exactly two islands in grid.
'''