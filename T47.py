import copy
class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        #处理方法，规定一种使用顺序，比如，规定相等的数字index小的那个不能再index大的那个后面，这样就避免了小的用来造一次，大的还被使用
        res = []
        oneRes = []
        nums.sort()
        visited = [0]*len(nums)
        self.permu(res,oneRes,nums,visited)
        return res

    def permu(self,res,oneRes,nums, visited):
        if len(oneRes) ==len(nums):
            res.append(copy.deepcopy(oneRes))
            return
        for i in range(len(nums)):
            #已经用过，就不再用
            if visited[i]:continue
            #如果这个index是相同数字,且上一个相同的数字没有被使用，这个也不能用
            if (i>0 and nums[i]==nums[i-1] and not visited[i-1]):continue
            visited[i]=1
            oneRes.append(nums[i])
            self.permu(res,oneRes,nums,visited)
            oneRes.pop()
            visited[i]=0




'''
47. Permutations II
Medium
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10
'''