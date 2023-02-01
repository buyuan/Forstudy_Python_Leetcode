class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #1 反对角线反转
        self.anti_diagonal_rev(matrix)
        #2 中线上下翻转
        self.middleLine_rev(matrix)

    def anti_diagonal_rev(self, matrix):
        #matrix[i][j] =matrix[len-1-j][len-1-i];
        length = len(matrix)
        for i in range(0,length):
            for j in range(length-1-i,-1,-1):
                cur = matrix[i][j]
                matrix[i][j] =matrix[length-1-j][length-1-i]
                matrix[length - 1 - j][length - 1 - i] = cur

    def middleLine_rev(self, matrix):
        #matrix[i][j] = matrix[len-1-i][j];
        length = len(matrix)
        for i in range(0, int(length/2)):
            for j in range(0, length):
                cur = matrix[i][j]
                matrix[i][j] = matrix[length-1-i][j]
                matrix[length-1-i][j] = cur

'''
48. Rotate Image
Medium
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.



Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
Example 2:


Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]


Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000

'''