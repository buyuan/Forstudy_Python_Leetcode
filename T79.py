import copy


class Solution:

    def exist(self, board: list[list[str]], word: str) -> bool:
        #先找到第一个字母，然后从此开始前进和回溯,需要有个set记录已经访问过的，访问过的不能再访问,
        #注意，不应该用set记录，应该是用stack记录，这样不仅可以保留一访问的点，还能保证是上次的路径
        #需要用一个index记录上次进入循环的坐标，出来以后这之后的都删除
        #而且，在找到错误的路径后，对应的坐标应该从set中去掉
        ans = False
        #用全局变量，快一些
        self.board=board
        self.ROWS = len(board)
        self.COLS = len(board[0])

        for i in range(self.ROWS):
            for j in range(self.COLS):
                ans = self.search_New( word, i, j)
                if ans:
                    return ans
        return ans
    # 下面这个会超时，这个case
    '''
        board =
        [["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]]
        word =
        "AAAAAAAAAAAAAAa"
    '''
    def search_old(self,board: list[list[str]], subword: str,rol:int, col:int,stk) -> bool:
        if len(subword)==0:
            return True
        #向各个方向探索
        letter = subword[0]
        upLine,bottomLine,leftLine,rightLine = 0,len(board)-1,0,len(board[0])-1
        ans = False
        startPoint = len(stk)
        #上
        if rol>upLine and board[rol-1][col]==letter and not stk.__contains__(str(rol-1)+str(col)):
            stk.append(str(rol-1) + str(col))
            ans = self.search(board, subword[1:], rol-1, col,stk)
            if ans:
                return ans
        #下
        if rol<bottomLine and board[rol+1][col]==letter and not stk.__contains__(str(rol+1)+str(col)):
            #要把统一轮的其他点吐出来，才能保证是原始状态
            stk = stk[:startPoint]
            stk.append(str(rol+1)+str(col))
            ans = self.search(board, subword[1:], rol+1, col,stk)
            if ans:
                return ans
        #左
        if col>leftLine and board[rol][col-1]==letter and not stk.__contains__(str(rol)+str(col-1)):
            stk = stk[:startPoint]
            stk.append(str(rol) + str(col-1))
            ans = self.search(board, subword[1:], rol, col-1,stk)
            if ans:
                return ans
        #右
        if col<rightLine and board[rol][col+1]==letter and not stk.__contains__(str(rol)+str(col+1)):
            stk = stk[:startPoint]
            stk.append(str(rol) + str(col +1))
            ans = self.search(board, subword[1:], rol, col+1,stk)
            if ans:
                return ans

        return ans
    #这个是对上面的一些小优化,还是超时
    def search(self, board: list[list[str]], subword: str, rol: int, col: int, stk) -> bool:
        if len(subword)==0:
            return True
        #向各个方向探索
        letter = subword[0]
        if rol<0 or rol>len(board)-1 or col<0 or col>len(board[0])-1 \
                or board[rol][col] != letter or stk.__contains__(str(rol)+str(col)):
            return False
        endPoint = len(stk)
        stk.append(str(rol) + str(col))
        #需要走一次清空一次，不然别的路线走过的就会干扰
        ans = False
        for rowOffset, colOffset in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
            ans = self.search(board,subword[1:],rol + rowOffset, col + colOffset, stk)
            # break instead of return directly to do some cleanup afterwards
            if ans: break
        #当前点的路径往后走不能出现在下一次调用中，所以还原
        stk.pop()
        return ans

    #改用原来的二维数组记录 已经访问的
    def search_New(self, subword: str, rol: int, col: int) -> bool:
        if len(subword)==0:
            return True
        #向各个方向探索
        letter = subword[0]
        if rol<0 or rol==self.ROWS or col<0 or col==self.COLS \
                or self.board[rol][col] != letter :
            return False
        self.board[rol][col] ="&"
        #需要走一次清空一次，不然别的路线走过的就会干扰
        ans = False
        for rowOffset, colOffset in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
            ans = self.search_New(subword[1:],rol + rowOffset, col + colOffset)
            # break instead of return directly to do some cleanup afterwards
            if ans: break
        #当前点的路径往后走不能出现在下一次调用中，所以还原
        self.board[rol][col] =letter
        return ans
'''
79. Word Search
Medium
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.



Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false


Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.

'''