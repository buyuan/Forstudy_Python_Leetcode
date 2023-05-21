from collections import deque


class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        #所有的1开始，每次扩展一圈，这一圈是指上下左右这种一步的圈，扩展的步数填入表，这个然后从这一圈新的点继续扩展，知道所有点都扩展完
        que = deque()
        #遍历找到所有的1，作为初始开始的点
        height,width = len(grid),len(grid[0])
        for r in range(height):
            for c in range(width):
                if grid[r][c]==1:
                    que.append([r,c])
        #没有1，或者没有0，返回-1
        if not que or len(que)==height*width:return -1

        dirIndex = [0,1,0,-1,0]
        step=0
        while que:
            size = len(que)
            step+=1
            while size>0:
                size-=1
                r,c = que.popleft()
                for i in range(4):
                    nr,nc = r+dirIndex[i],c+dirIndex[i+1]
                    #越界或者不是0,不用遍历
                    if nr<0 or nr>height-1 or nc<0 or nc>width-1 or grid[nr][nc]!=0:continue
                    grid[nr][nc]=step
                    que.append([nr,nc])
        #最后找到的那个0就是距离所有1都是最远的0，（因为所有1一期开始遍历的）
        #step -1是因为，最后一个点会进入que，然后找不到可以遍历的，但是step已经+1了
        return step-1
'''
1162. As Far from Land as Possible
Medium
Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return -1.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.



Example 1:


Input: grid = [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.
Example 2:


Input: grid = [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation: The cell (2, 2) is as far as possible from all the land with distance 4.


Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1
'''