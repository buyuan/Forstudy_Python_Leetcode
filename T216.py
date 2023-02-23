class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        # 类似40，且没有重复值,但是答案中的数组，数字个数为k
        # 方法，排序数组，然后循环到和前一个相同的数字时，跳过，因为如果是需要连续相同的数字，第一个就能找全，如果不需要，
        # 即只要这一个数字的时候，跳后后面相同的就可以
        temp = []
        ans = []
        self.findCombi(ans, temp, k, n, 1)
        return ans

    def findCombi(self, ans:list[list[int]], temp:list[int], k:int, target:int, startpoint:int):
        if k<0 or target<0:return
        if k==0 and target ==0:
            ans.append(temp.copy())
            return
        for i in range(startpoint,10):
            temp.append(i)
            self.findCombi(ans, temp, k-1, target-i, i+1)
            temp.pop()


'''
216. Combination Sum III
Medium
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.



Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.
Example 3:

Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.


Constraints:

2 <= k <= 9
1 <= n <= 60
'''