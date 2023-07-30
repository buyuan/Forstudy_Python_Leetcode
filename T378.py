class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        def smallerOrEqual(mid):
            res=0
            m,n = len(matrix),len(matrix[0])
            i,j=m-1,0
            while i>=0 and j<n:
                if matrix[i][j]<=mid:
                    #i行j列往上的都比mid小，然后测试这个点的后面一个
                    res+=i+1
                    j+=1
                else:
                    i-=1
            return res

        #binary search，判断小于mid的有多少个数字
        lower,upper = matrix[0][0],matrix[-1][-1]
        while lower<upper:
            mid = lower+(upper-lower)//2
            count = smallerOrEqual(mid)
            if count<k:
                #mid小了
                lower=mid+1
            else:
                upper=mid
        return lower




'''
378. Kth Smallest Element in a Sorted Matrix
Medium
Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n2).

 

Example 1:

Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
Example 2:

Input: matrix = [[-5]], k = 1
Output: -5
 

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 300
-109 <= matrix[i][j] <= 109
All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
1 <= k <= n2
 

Follow up:

Could you solve the problem with a constant memory (i.e., O(1) memory complexity)?
Could you solve the problem in O(n) time complexity? The solution may be too advanced for an interview but you may find reading this paper fun.
'''