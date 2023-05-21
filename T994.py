from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        #先遍历一次，找到初始的所有坏橘子，然后扩展，扩展一次就是1分钟，扩展到无法扩展，然后再扫描一下，看看还有没有坏橘子
        #改成记录一下有多少个好的，然后记录有多少重新腐烂的，比较数字是否相等，减少再一次遍历
        que = deque()
        #find the initial node
        height,width = len(grid),len(grid[0])
        cnt_fresh=0
        for r in range(height):
            for c in range(width):
                if grid[r][c]==2:
                    que.append([r,c])
                elif grid[r][c]==1:
                    cnt_fresh+=1
        # 没有水果
        if not que and cnt_fresh == 0: return 0
        # 没有烂水果
        if not que: return -1
        # 没有好水果
        if cnt_fresh == 0: return 0

        #开始扩展
        res = 0
        cnt_rot=0
        while que:
            size = len(que)
            res+=1
            while size>0:
                size -= 1
                r,c = que.popleft()
                #四面扩展
                indexList = [0,1,0,-1,0]
                for i in range(4):
                    nr = r+indexList[i]
                    nc = c+indexList[i+1]
                    #越界或者没有橘子，或者已经腐烂，不处理
                    if nr<0 or nr>height-1 or nc<0 or nc>width-1 or grid[nr][nc]==0 or grid[nr][nc]==2:continue
                    grid[nr][nc]=2
                    cnt_rot+=1
                    que.append([nr,nc])

        #因为最后一轮的腐烂节点，再无更多的橘子可以腐烂，但是仍然会进入一次循环，所以结果多加了1
        return res-1 if cnt_rot==cnt_fresh else -1





'''
994. Rotting Oranges
Medium
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.



Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
'''