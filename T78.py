import copy


class Solution:
    def dfs_combi(self,nums: list[int], start: int, cur: list[int], targetLen: int, ans: list[list[int]]):
        if len(cur) == targetLen :
            ans.append(copy.deepcopy(cur))
            return

        for index in range(start, len(nums)):
            cur.append(nums[index])
            self.dfs_combi(nums,index+1,cur,targetLen,ans)
            cur.pop()


    def subsets(self, nums: list[int]) -> list[list[int]]:
        #combination
        #C(m,n)
        ans = []
        cur = []
        for i in range(0, len(nums)+1):
            self.dfs_combi(nums,0,cur,i,ans)
        return ans

'''
78. Subsets
Medium
185
company
Amazon
company
Bloomberg
company
Facebook
Given an integer array nums of unique elements, return all possible
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
'''