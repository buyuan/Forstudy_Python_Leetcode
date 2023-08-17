class TrieNode:
    def __init__(self,val=''):
        self.child={}
        self.isWord=False
        self.curLetter=val
class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        def buildTrie(words):
            rt = TrieNode()
            for word in words:
                cur = rt
                for chr in word:
                    if chr not in cur.child:
                        cur.child[chr] = TrieNode(chr)
                    cur = cur.child[chr]
                cur.isWord=True
            return rt

        if not words or not board:return []
        root = buildTrie(words)
        ans = []
        for x, r in enumerate(board):
            for y, c in enumerate(r):
                #x,y是坐标，c是坐标的字符
                if c in root.child:
                    #能找到，继续
                    self.search(board,x,y,root.child[c],c,ans)
        return ans

    def search(self,board,x,y,nd,word,ans):
        if nd.isWord:
            ans.append(word)
            nd.isWord=False
        if not len(nd.child):return
        temp = board[x][y]
        board[x][y] = "&"
        #增加一步，只有下一个匹配才进入递归，减少不必要的递归调用
        index = [-1,0,1,0,-1]
        for i in range(4):
            nx,ny = x+index[i],y+index[i+1]
            if nx<0 or nx>=len(board) or ny<0 or ny>=len(board[0]) or board[nx][ny] not in nd.child:
                continue
            c = board[nx][ny]
            self.search(board,nx,ny,nd.child[c],word+c,ans)

        board[x][y] =temp
 



    #还是超时，不过大体过成诗对的，我再优化一下
    def findWords_old2(self, board: list[list[str]], words: list[str]) -> list[str]:
        #创建一个前缀树，这样的话，只用扫一遍前缀树就可以了
        class TrieNode:
            def __init__(self):
                self.subNode = [None]*26
                self.isWord=False
                self.curWord = ""
                self.curLetter=''
        root = TrieNode()
        for word in words:
            cur = root
            for i in range(len(word)):
                index = ord(word[i])-ord('a')
                if not cur.subNode[index]:
                    temp = cur.curWord
                    cur.subNode[index]=TrieNode()
                    cur = cur.subNode[index]
                    cur.curWord=temp+word[i]
                    cur.curLetter=word[i]
                else:
                    cur = cur.subNode[index]
                if i==len(word)-1:
                    cur.isWord=True

        #然后遍历这个数组
        self.ans =[]
        Row,Col = len(board),len(board[0])
        for r in range(Row):
            for c in range(Col):
                index = ord(board[r][c])-ord('a')
                node = root.subNode[index]
                self.search(board,r,c,node,Row,Col)
        return self.ans

    def search(self,board,r,c,node,Row,Col):
        if not node:return
        #遍历这个root，如果发现isword，则加入答案
        if r<0 or r>=Row or c<0 or c>=Col or board[r][c]!=node.curLetter:
            return
        if node.isWord :
            self.ans.append(node.curWord)
            node.isWord=False
        for nd in node.subNode:
            if nd:
                temp = board[r][c]
                board[r][c]="%"
                #不为空就继续往下遍历   
                self.search(board,r+1,c,nd,Row,Col)
                self.search(board,r-1,c,nd,Row,Col)
                self.search(board,r,c+1,nd,Row,Col)
                self.search(board,r,c-1,nd,Row,Col)
                board[r][c]=temp




    ####Below Time Limit Exceeded
    def findWords_old(self, board: list[list[str]], words: list[str]) -> list[str]:
        #每个单词都单独找一遍，看能不能找到
        ans=[]
        for word in words:
            if self.contains(word,board):
                ans.append(word)
        return ans
    
    def contains(self,target, board):

        Row = len(board)
        Col = len(board[0])
        def search(target,cur,r,c):
            #如果越界或者这个坐标和目标的字符不符合，返回false
            if r<0 or r>=Row or c<0 or c>=Col or target[cur]!=board[r][c]:
                return False
            if cur==len(target)-1:
                #找完了都没有出现错误，说明存在
                return True
            temp = board[r][c]
            board[r][c] = "*"
            #继续往后递归
            found = search(target,cur+1,r+1,c) or search(target,cur+1,r-1,c) or search(target,cur+1,r,c+1) or search(target,cur+1,r,c-1)
            board[r][c] = temp
            return found

        for i in range(Row):
            for j in range(Col):
                if search(target,0,i,j):
                    #从单词的第0个字母开始，从第i,j坐标开始找，如果能找完target，就返回True
                    return True
        return False

        
'''
212. Word Search II
Hard
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example 1:


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:


Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.'''