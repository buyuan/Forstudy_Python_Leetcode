class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #从左到右，从上到下遍历，以及回溯，每填一个数字，验证是否合适，如果当走完9行，说明完成，
        self.helper(board,0,0)

    def helper(self, board, row, col)->bool:
        #用bool，是因为在return的时候方便进入helper，同时可以稍微用于反应是否完成，其实用其他类型也一样
        #所有行都跑完，可以结束了
        if row>=9:return True
        #当前行跑完，进入下一行
        if col>=9:return self.helper(board,row+1,0)
        #这个位置有数字了，继续下一个位置
        if board[row][col]!='.':return self.helper(board,row,col+1)
        #其他情况，开始填数字：
        for ch in ['1','2','3','4','5','6','7','8','9']:
            #如果这个ch填入当前的点合法，就可以继续
            if self.isValid(board,row,col,ch):
                board[row][col] = ch
                #然后继续往后遍历，如果成功就不用继续了
                if self.helper(board,row,col+1):return True
                # 如果刚才那个不行，返回初始状态,继续下一个值尝试
                else:board[row][col] = '.'
        return False

    def isValid(self, board, row, col, ch):
        #同一行没有相同的：
        for i in range(9):
            if board[row][i]==ch:return False
        #统一列没有相同的：
        for i in range(9):
            if board[i][col]==ch:return False
        #同一个方格没有相同：
        #row,col所属方格的左上角坐标
        i,j= row-row%3,col-col%3
        for x in range(3):
            for y in range(3):
                if board[x+i][y+j]==ch:return False
        return True

'''
37. Sudoku Solver
Hard
Write a program to solve a Sudoku puzzle by filling the empty cells.
A sudoku solution must satisfy all of the following rules:
Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.
Example 1:
Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:
Constraints:
board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.
'''