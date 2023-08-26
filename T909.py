from collections import deque


class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        #BFS 从1开始，每次移动，可以移动+1，到+6，然后把这些结果入栈，进行下一轮移动， 什么时候，某一个起点移动到左上角了，就停止，此时的移动步数是最少的
        n = len(board)
        #用下标作为移动数字所以是从1到n*n
        visited = [0]*(n*n+1)
        q = deque()
        q.append(1)
        visited[1]=1
        steps=0
        #先把答案放到最大值
        ans=n*n
        while q:
            size = len(q)
            for i in range(size):
                curPosition = q.popleft()
                if curPosition==n*n:
                    #走到了最后
                    ans = min(ans,steps)
                #开始这个位置可能的6个终点的扩散
                for j in range(1,7):
                    nextP = curPosition+j
                    if nextP>n*n:break
                    if visited[nextP]:continue
                    visited[nextP]=1
                    r, c = self.getPosition(n,nextP)
                    if board[r][c]==-1:
                        #普通的点
                        q.append(nextP)
                    elif board[r][c]==nextP:
                        #回到原点，会有循环，跳过
                        continue
                    else:
                        #梯子，蛇
                        q.append(board[r][c])
            steps+=1
        
        if ans==n*n:
            #遇到循环走不过去
            return -1
        else:
            return ans
    
    def getPosition(self,n,num):
        #用前一个位置判断r，以免出现刚好在一行最后一个位置上
        r = n-(num-1)//n-1
        #(n-r)%2不能整除就是右到左变大，能整除就是左到右变大
        c =  n-(num-1)%n-1 if (n-r)%2 ==0 else (num-1)%n
        return (r,c)






'''
909. Snakes and Ladders
Medium
You are given an n x n integer matrix board where the cells are labeled from 1 to n2 in a Boustrophedon style starting from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.

You start on square 1 of the board. In each move, starting from square curr, do the following:

Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n2)].
This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations, regardless of the size of the board.
If next has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to next.
The game ends when you reach the square n2.
A board square on row r and column c has a snake or ladder if board[r][c] != -1. The destination of that snake or ladder is board[r][c]. Squares 1 and n2 do not have a snake or ladder.

Note that you only take a snake or ladder at most once per move. If the destination to a snake or ladder is the start of another snake or ladder, you do not follow the subsequent snake or ladder.

For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination square is 2. You follow the ladder to square 3, but do not follow the subsequent ladder to 4.
Return the least number of moves required to reach the square n2. If it is not possible to reach the square, return -1.

 

Example 1:


Input: board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
Output: 4
Explanation: 
In the beginning, you start at square 1 (at row 5, column 0).
You decide to move to square 2 and must take the ladder to square 15.
You then decide to move to square 17 and must take the snake to square 13.
You then decide to move to square 14 and must take the ladder to square 35.
You then decide to move to square 36, ending the game.
This is the lowest possible number of moves to reach the last square, so return 4.
Example 2:

Input: board = [[-1,-1],[-1,3]]
Output: 1
 

Constraints:

n == board.length == board[i].length
2 <= n <= 20
board[i][j] is either -1 or in the range [1, n2].
The squares labeled 1 and n2 do not have any ladders or snakes.'''