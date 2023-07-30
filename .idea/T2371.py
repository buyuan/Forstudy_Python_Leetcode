class Solution:
    def minScore(self, grid: list[list[int]]) -> list[list[int]]:
        #先用值排序，直到一个递增的坐标的顺序，这个排序实际也可以看成row和col的分开排序，这个顺序对应的坐标是保持原grid的顺序的。
        #然后依次按照这个坐标位置递增
        #在递增的时候，记录行，列的当前最小值，然后从其中选择一个更大的作为当前点点最大值，然后行列最小值遍历到下个
        
        R,C = len(grid),len(grid[0])
        r_min,c_min = [1]*R,[1]*C

        #value，point tuple
        seq = [(grid[i][j],i,j) for i in range(R) for j in range(C)]
        seq.sort(key= lambda x:x[0])

        #遍历所有的点
        for i in range(len(seq)):
            _,r,c = seq[i]
            #这个点从行从列看都需要是最大的（生序）
            grid[r][c] = max(r_min[r],c_min[c])
            #这个点占据之后，相同行，列的值的可用的最小值都要+1,保持下一个生序的点的值是生序
            r_min[r] = grid[r][c]+1
            c_min[c] = grid[r][c]+1
        return grid

'''
2371. Minimize Maximum Value in a Grid
Hard
You are given an m x n integer matrix grid containing distinct positive integers.

You have to replace each integer in the matrix with a positive integer satisfying the following conditions:

The relative order of every two elements that are in the same row or column should stay the same after the replacements.
The maximum number in the matrix after the replacements should be as small as possible.
The relative order stays the same if for all pairs of elements in the original matrix such that grid[r1][c1] > grid[r2][c2] where either r1 == r2 or c1 == c2, then it must be true that grid[r1][c1] > grid[r2][c2] after the replacements.

For example, if grid = [[2, 4, 5], [7, 3, 9]] then a good replacement could be either grid = [[1, 2, 3], [2, 1, 4]] or grid = [[1, 2, 3], [3, 1, 4]].

Return the resulting matrix. If there are multiple answers, return any of them.

 

Example 1:


Input: grid = [[3,1],[2,5]]
Output: [[2,1],[1,2]]
Explanation: The above diagram shows a valid replacement.
The maximum number in the matrix is 2. It can be shown that no smaller value can be obtained.
Example 2:

Input: grid = [[10]]
Output: [[1]]
Explanation: We replace the only number in the matrix with 1.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 1000
1 <= m * n <= 105
1 <= grid[i][j] <= 109
grid consists of distinct integers.
'''