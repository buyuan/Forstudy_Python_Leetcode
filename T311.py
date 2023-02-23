class Solution:
    def multiply(self, mat1: list[list[int]], mat2: list[list[int]]) -> list[list[int]]:
        ans = []
        for m in range(len(mat1)):
            #row
            temp = []
            for n in range(len(mat2[0])):
                #col
                cur = 0
                k=0
                while k<len(mat1[0]) and k<len(mat2):
                    a = mat1[m][k]
                    b=  mat2[k][n]
                    cur += mat1[m][k]*mat2[k][n]
                    k+=1
                temp.append(cur)
            ans.append(temp)
        return ans

'''
311. Sparse Matrix Multiplication
Medium
Given two sparse matrices mat1 of size m x k and mat2 of size k x n, return the result of mat1 x mat2. You may assume that multiplication is always possible.
Example 1:
Input: mat1 = [[1,0,0],[-1,0,3]], mat2 = [[7,0,0],[0,0,0],[0,0,1]]
Output: [[7,0,0],[-7,0,3]]
Example 2:
Input: mat1 = [[0]], mat2 = [[0]]
Output: [[0]]
Constraints:
m == mat1.length
k == mat1[i].length == mat2.length
n == mat2[i].length
1 <= m, n, k <= 100
-100 <= mat1[i][j], mat2[i][j] <= 100
'''