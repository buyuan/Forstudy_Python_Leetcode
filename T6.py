class Solution:
    def convert(self, s: str, numRows: int) -> str:
        #find a way to get the movement of index
        #一组实际是 numRows+numRows-2的字母数量(除了第一行满numRows，后面numRow-2行，只有numRow-2个字母)\\
        if numRows==1:
            return s
        elif numRows>2:
            width = ((len(s)//(numRows+numRows-2))+1)*(numRows-1)
        else:
            width = (len(s)//numRows) +1
        board = [[0]*width for i in range(numRows)]
        r,c=0,0
        downFlag=True
        for chr in s:
            board[r][c] = chr
            if r==numRows-1:
                downFlag=False
            if not downFlag:
                #往上走的情况
                r-=1
                c+=1
                if r==0:
                    downFlag=True
            else:
                r+=1
        res=""
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c]==0:
                    continue
                else:
                    res+=board[r][c]
        return res