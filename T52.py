class Solution:
    def __init__(self):
        self.res=0
    def totalNQueens(self, n: int) -> int:
        #参考51，只不过这次不用写出具体解
        curQueen =[[0 for i in range(n)] for j in range(n)]
        self.helper(0,curQueen)
        return self.res

    def helper(self, curRow, curQueen):
        length = len(curQueen)
        if curRow==length:
            self.res+=1
            return

        for i in range(length):
            #开始回溯，
            if self.isValid(curQueen, curRow, i):
                curQueen[curRow][i]=1
                self.helper(curRow+1,curQueen)
                curQueen[curRow][i] = 0

    def isValid(self,curQueen,row,col):
        for i in range(row):
            #同一列是否存在1
            if curQueen[i][col]:return False
        for i ,j in zip(range(row-1,-1,-1), range(col-1,-1,-1)):
            #对角线
            if curQueen[i][j]: return False
        for i ,j in zip(range(row-1,-1,-1), range(col+1,len(curQueen))):
            #反对角线
            if curQueen[i][j]: return False
        return True


'''
52. N-Queens II
Hard
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example 1:


Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
Example 2:

Input: n = 1
Output: 1
'''