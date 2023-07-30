
from collections import deque


class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        #正常的BFS扫描，计数，遇到岛的边界在边上，计数，然后减去边界的岛
        q=deque()
        res=0
        direction = [0,1,0,-1,0]
        m,n = len(grid),len(grid[0])
        def is_boundary(x,y):
            #判断x是否在边界
            if x==0 or y==0 or x==m-1 or y==n-1 :
                return True
            return False
        for i in range(m):
            for j in range(n):
                if grid[i][j]==9 or grid[i][j]==0:
                    #visited or not island
                    continue
                if grid[i][j] == 1:
                    q.append((i,j))
                    grid[i][j]=9
                #开始蔓延这个岛屿
                boundary=False
                cellNo=0
                while q:
                    x,y = q.popleft()
                    cellNo+=1
                    #每次是一个岛屿，所以在这个地方判断是否有边界岛屿
                    if not boundary and is_boundary(x,y):
                        boundary=True
                    for d in range(4):
                        nx,ny=x+direction[d],y+direction[d+1]
                        if nx<0 or ny<0 or nx>=m or ny>=n:continue
                        if grid[nx][ny]==1:
                            q.append((nx,ny))
                            grid[nx][ny]=9
                if not boundary:
                    res+=cellNo
        return res
                    
                    

'''
1020. Number of Enclaves
Medium
You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

 

Example 1:


Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.
Example 2:


Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: All 1s are either on the boundary or can reach the boundary.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 500
grid[i][j] is either 0 or 1.'''