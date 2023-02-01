import copy

class Solution:
    def dfs_com(self, nums: list[int], cur: list[int], ans: list[list[int]],targetLen: int, startIndex: int):
        if len(cur) == targetLen:
            ans.append(copy.deepcopy(cur))
            return
        for i in range(startIndex, len(nums)):
            #remember I does not always start from 0
            if i>startIndex and nums[i] == nums[i-1]:
                continue
            cur.append(nums[i])
            self.dfs_com(nums,cur, ans, targetLen,i+1)
            cur.pop()

    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nNums = sorted(nums)
        cur = []
        result=[]
        for i in range(0, len(nNums)+1):
            self.dfs_com(nNums,cur, result, i,0)
        return result



'''
90. Subsets II
Medium
Given an integer array nums that may contain duplicates, return all possible
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
'''