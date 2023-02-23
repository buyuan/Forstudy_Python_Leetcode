


class Solution:
    pLevel = [0,[1],[1,1]]
    len = 2
    def getPn(self, n:int)->list[int]:
        if n <=Solution.len:
            return Solution.pLevel[n]
        else:
            plast = self.getPn(n-1)
        pn = [1]
        for i in range(1,n-1):
            pn.append(plast[i-1]+plast[i])
        pn.append(1)
        Solution.pLevel.append(pn)
        Solution.len += 1
        return pn
    def generate(self, numRows: int) -> list[list[int]]:
        ans =[]
        for i in range(1,numRows+1):
            ans.append(self.getPn(i))
        return ans
'''
118. Pascal's Triangle
Easy
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]


Constraints:

1 <= numRows <= 30
'''