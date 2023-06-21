from collections import deque


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        #用BFS做一下
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    res+=1
                    self.BFS(i,j,grid)
        return res
    def BFS(i,j,grid):
        q = deque()
        q.append([i,j])
        index = [-1,0,1,0,-1]
        grid[i][j]='0'
        while q:
            curPoint =q.pop()
            for x in range(4):
                ni ,nj= curPoint[0]+index[x],curPoint[1]+index[x+1]
                if ni<0 or ni>=len(grid) or nj<0 or nj>=len(grid[0]) or grid[ni][nj]=='0':
                    continue
                q.append([ni,nj])
                grid[ni][nj]='0'
'''
200. Number of Islands
Medium
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
'''