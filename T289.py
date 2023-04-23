class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #用二进制数表示前后两个状态， 后/前，比如， 10，就是说，一开始是0，后来是1，所以在扫描的时候
        #既可以知道下一个状态，也可以保留当前状态，在用二进制找当前状态是时，也有一个方便的方法，
        #用新的值&&1， 这样，如果结果是0，说明当前状态是0，是1则表明当前是1
        for i in range(len(board)):
            for j in range(len(board[0])):
                neighbourCheck = self.check(board,i,j)
                if board[i][j]==1:
                    if neighbourCheck==2 or neighbourCheck==3:
                        #二进制1，1
                        board[i][j]=3
                elif  board[i][j]==0:
                    if neighbourCheck==3:
                        board[i][j] =2
        #扫描，更新为下一个状态，更新方法，board[i][j] 右移动一位
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j]= board[i][j]>>1

    def check(self, board, row, col):
        #check有一个好方法，就是用board[i][j] && 1， 这样结果就能轻易知道原来的第一位是什么，如果结果是1，原来是1，如果是0，原来是0
        #range x j-1,j.j+1, range y i-1,i,i+1
        count=0
        for y in range(max(0,row-1),min(len(board),row+2)):
            for x in range(max(0,col-1),min(len(board[0]),col+2)):
                if y==row and x == col:continue
                if board[y][x]&1==1:
                    #是1
                    count+=1
        return count



'''
289. Game of Life
Medium
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.



Example 1:


Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
Example 2:


Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]


Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 25
board[i][j] is 0 or 1.

'''