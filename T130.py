class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #从边上找，找到O，遍历完这一坨先改成别的字符，然后其他的O都是中间的，改成X，然后再把别的符号改回O
        width, height = len(board[0]),len(board)
        def dfs(row, col,board):
            board[row][col]="$"
            #查看上下左右是不是有O
            #上
            if row-1>=0 and board[row-1][col]=="O":
                dfs(row-1,col,board)
            #下
            if row+1<=height-1 and board[row+1][col]=="O":
                dfs(row + 1, col, board)
            #左：
            if col-1>=0 and board[row][col-1]=="O":
                dfs(row,col-1,board)
            #右
            if col+1<=width-1 and board[row][col+1]=="O":
                dfs(row, col+1, board)

        #up and down
        for col in range(width):
            if board[0][col]=='O':
                dfs(0,col,board)
            if board[height-1][col]=='O':
                dfs(height-1,col,board)
        #left and right
        for row in range(height):
            if board[row][0]=="O":
                dfs(row,0,board)
            if board[row][width-1]=="O":
                dfs(row,width-1,board)
        # replace
        for i in range(height):
            for j in range(width):
                if board[i][j]=="O":
                    board[i][j] = "X"
                elif board[i][j]=="$":
                    board[i][j] = "O"




'''
130. Surrounded Regions
Medium
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

 

Example 1:


Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.
Example 2:

Input: board = [["X"]]
Output: [["X"]]


Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
'''