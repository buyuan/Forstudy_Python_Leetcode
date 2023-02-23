class Solution:
    pLevel = [[1], [1, 1]]
    len = 2
    def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex <= Solution.len-1:
            return Solution.pLevel[rowIndex-1]
        else:
            plast = self.getRow( rowIndex- 1)
        pn = [1]
        for i in range(1, rowIndex ):
            pn.append(plast[i - 1] + plast[i])
        pn.append(1)
        Solution.pLevel.append(pn)
        Solution.len += 1
        return pn


'''
119. Pascal's Triangle II
Easy
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:




Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]


Constraints:

0 <= rowIndex <= 33
'''