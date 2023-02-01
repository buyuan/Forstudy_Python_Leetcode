class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result =[]
        #1. sort
        for i in range(1, len(nums)):
            j = i
            temp = nums[j]
            while j > 0 and temp < nums[j-1]:
                nums[j] = nums[j-1]
                j-=1
            nums[j]=temp
        #2 .start from some num, then find the part which sum to 0-this num
        for i in range(0,len(nums)):
            #剪枝
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                #防止重复结果因为这个值已经找过了
                continue
            target = 0-nums[i]
            left, right = i+1 , len(nums)-1
            while left<right :
                if nums[left]+nums[right]==target:
                    result.append([nums[i], nums[left], nums[right]])
                    #排除相等值
                    left+=1
                    right-=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    continue
                elif nums[left]+nums[right]>target:
                    right-=1
                else:
                    left+=1
        return result

''' 
15. 3Sum
Medium
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.


Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''