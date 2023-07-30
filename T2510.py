class Solution:

    def isThereAPath_dfs(self, grid: list[list[int]]) -> bool:
        #non_recursion
        m,n= len(grid),len(grid[0])
        stk=[]
        stk.append((0,0,0))
        visited=set()
        while stk:
            cur = stk.pop()
            if not visited.__contains__(cur):
                visited.add(cur)
                x,y,count = cur
                if grid[x][y]==0:
                    count-=1
                else:
                    count+=1
                if x==m-1 and y==n-1:
                    if count==0:return True
                else:
                    nx1,ny1 = x+1,y
                    if nx1<m and ny1<n:
                        stk.append((nx1,ny1,count))
                    nx2,ny2 = x,y+1
                    if nx2<m and ny2<n:
                        stk.append((nx2,ny2,count))
        return False


    def isThereAPath_DFS(self, grid: list[list[int]]) -> bool:
        #DFS,递归
        m,n=len(grid),len(grid[0])
        #做一些剪枝，把，（x,y,count）作为一个点的标记，这样走到x,y且已经计数过的就不用再走，因为前面相同结果的已经跑过了
        visited=set()
        def helper(i,j,count):
            if not visited.__contains__((i,j,count)):
                visited.add((i,j,count))
                if i>=m or j >=n:
                    return False
                if grid[i][j]==0:
                    count-=1
                else:
                    count+=1
                if i==m-1 and j==n-1:
                    #走到右下角
                    return count==0
                return helper(i+1,j,count) or helper(i,j+1,count)
            else:
                return False
        return helper(0,0,0)



'''
2510. Check if There is a Path With Equal Number of 0's And 1's
Medium
You are given a 0-indexed m x n binary matrix grid. You can move from a cell (row, col) to any of the cells (row + 1, col) or (row, col + 1).

Return true if there is a path from (0, 0) to (m - 1, n - 1) that visits an equal number of 0's and 1's. Otherwise return false.

 

Example 1:


Input: grid = [[0,1,0,0],[0,1,0,0],[1,0,1,0]]
Output: true
Explanation: The path colored in blue in the above diagram is a valid path because we have 3 cells with a value of 1 and 3 with a value of 0. Since there is a valid path, we return true.
Example 2:


Input: grid = [[1,1,0],[0,0,1],[1,0,0]]
Output: false
Explanation: There is no path in this grid with an equal number of 0's and 1's.
 

Constraints:

m == grid.length
n == grid[i].length
2 <= m, n <= 100
grid[i][j] is either 0 or 1.'''