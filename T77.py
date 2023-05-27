
import copy


class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        #回溯，从某个start开始，往start+1到end找结果，然后跳出来，回到原状态
        res = []
        oneRes= []
        self.backTrace(res,oneRes,1,k,n)
        return res
    def backTrace(self,res,oneRes,start,k,n):
        if len(oneRes) ==k:
            res.append(copy.deepcopy(oneRes))
            return
        for i in range(start,n+1):
            oneRes.append(i)
            self.backTrace(res,oneRes,i+1,k,n)
            oneRes.pop()

'''
77. Combinations
Medium
6K
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

 

Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.
 

Constraints:

1 <= n <= 20
1 <= k <= n
'''