class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        #思路就是，参考84题，最大直方图面积那个，依次把每一行当作直方图底边，计算最大面积
        #例如，4X5的矩阵，如果把第三行当成底边，那么第一，第二行，第三行，就是一个以第三行为底的底边
        ans=0
        for i in range(len(matrix)):
            Histogram = self.getHistogram(matrix,i)
            #然后开始用栈维护一个递增的方块（数组），当发现新的节点小于上一个节点时候，开始从头遍历，找出最大值
            #之所以从递减开始，是因为最高的那个节点（递减的前一个）可以容纳前面所有的方块形成矩形,因此就不用挨个计算了
            stk=[]
            #补一个0，则强制最后一个节点可以被处理
            Histogram.append(0)
            startIndex=0
            for j in range(len(Histogram)):
                if not stk:
                    #空了以后要注意重新开始的起点是当前的j
                    startIndex=j
                while stk and Histogram[j]<Histogram[stk[-1]]:
                    #如果当前的数值变小，开始遍历计算面积
                    Height = Histogram[stk.pop()]
                    area = 0
                    if not stk :
                        area = Height*(j-startIndex)
                    else:
                        area = Height*(j-stk[-1]-1)
                    ans = max(ans,area)
                stk.append(j)
        return ans
    def getHistogram(self,matrix:list[list[str]],level:int)-> list[int]:
        #从底面往上加，如果遇到0就截止
        length = len(matrix[0])
        res = [0]*length
        for i in range(length):
            cur = 0
            for j in range(level,-1,-1):
                temp = int(matrix[j][i])
                if temp==0:
                    break
                cur+=temp
            res[i] =cur
        return res

'''
85. Maximal Rectangle
Hard
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
Example 1:
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
Example 2:
Input: matrix = [["0"]]
Output: 0
Example 3:

Input: matrix = [["1"]]
Output: 1


Constraints:

rows == matrix.length
cols == matrix[i].length
1 <= row, cols <= 200
matrix[i][j] is '0' or '1'.
'''