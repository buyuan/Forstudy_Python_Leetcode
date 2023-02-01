class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        #先找到属于哪一行，然后在这一行做binary search

        index = -1
        for i in range(1,len(matrix)):
            if matrix[i][0]> target and matrix[i-1][0]<=target:
                index = i-1
                break
        if index==-1:
            #没找到，要么是在最后一行，或者比第一个数还小，要么就是没有
            if target<matrix[0][0]:
                return False
            if target<=matrix[len(matrix)-1][len(matrix[0])-1]:
                #在最后一行
                index = len(matrix)-1

        left , right = 0,len(matrix[0])
        while(left<right):
            mid = left+int((right-left)/2)
            if matrix[index][mid] == target:
                return True
            if matrix[index][mid]<target:
                left = mid+1
            else:
                right=mid
        return False


'''     
74. Search a 2D Matrix
Medium
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.



Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
'''