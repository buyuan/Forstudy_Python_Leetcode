from collections import deque


class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        #判断岛屿有没有接触边界
        q=deque()
        res=0
        m,n = len(grid),len(grid[0])
        def is_boundary(x,y):
            if x==0 or y==0 or x==m-1 or y==n-1:
                return True
            return False
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 or grid[i][j]==9:
                    #非岛屿或者已访问
                    continue
                q.append((i,j))
                grid[i][j]=9
                boundary = is_boundary(i,j)
                #遍历这个岛，如果岛临界边界，则不能加入答案
                direction=[-1,0,1,0,-1]
                while q:
                    x,y = q.popleft()
                    for k in range(4):
                        nx,ny = x+direction[k],y+direction[k+1]
                        if nx<0 or ny<0 or nx>m-1 or ny>n-1:continue
                        if grid[nx][ny]==0:
                            if not boundary and is_boundary(nx,ny):
                                boundary = True
                            grid[nx][ny]=9
                            q.append((nx,ny))
                if not boundary:
                    res+=1
        return res
                        
                        




'''
1254. Number of Closed Islands
Medium
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

 

Example 1:



Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).
Example 2:



Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1
Example 3:

Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2
 

Constraints:

1 <= grid.length, grid[0].length <= 100
0 <= grid[i][j] <=1
'''