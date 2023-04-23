


class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        res=[]
        curQueen=[['.' for i in range(n)] for j in range(n)]
        self.helper(0,curQueen,res)
        return res

    def helper(self, curRow, curQueen, res):
        length = len(curQueen)
        if curRow==length:
            #到最后一行也有效,可以加入答案了
            temp = []
            for line in curQueen:
                temp.append("".join(line))
            res.append(temp)
            return

        for i in range(length):
            if self.isValid(curRow,i,curQueen):
                #如果当前的位置[curRow,i]分布符合要求，赋值Q，继续下一行
                curQueen[curRow][i]='Q'
                self.helper(curRow+1,curQueen,res)
                #回来以后还原，准备转到另外的分支验证s
                curQueen[curRow][i] = '.'

    def isValid(self,row,col,curQueen):
        #同一列是否已有Q
        for i in range(row):
            if curQueen[i][col]=='Q':return False
        #对角线是否有Q,zip function是吧两个范围挨个变成1：1的tuple对，所以要求两个范围数量相等，正好适合对角线
        for i,j in zip(range(row-1,-1,-1),range(col-1,-1,-1)):
            if curQueen[i][j] == 'Q': return False
        #反对角线是否有Q
        for i,j in zip(range(row-1,-1,-1), range(col+1,len(curQueen))):
            if curQueen[i][j] == 'Q': return False
        return True
    

'''
51. N-Queens
Hard
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.
Example 1:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:
Input: n = 1
Output: [["Q"]]
Constraints:

1 <= n <= 9
'''