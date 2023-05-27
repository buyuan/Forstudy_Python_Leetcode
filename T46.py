import copy


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        #和组合不同的是，每次都要从第一个位置开始，
        res = []
        oneRes = []
        visited = [0]*len(nums)
        self.backTrack(res,oneRes,visited,nums)
        return res
    
    def backTrack(self,res,oneRes,visited,nums):
        '''
        parms:

        '''
        #还是一样的回溯，从头开始找下一个数字
        if len(oneRes) == len(nums):
            res.append(copy.deepcopy(oneRes))
            return 
        for i in range(len(nums)):
            if visited[i]==1:continue
            visited[i]=1
            oneRes.append(nums[i])
            self.backTrack(res,oneRes,visited,nums)
            oneRes.pop()
            visited[i]=0

'''
46. Permutations
Medium
15.6K
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.'''