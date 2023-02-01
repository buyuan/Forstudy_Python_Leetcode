import bisect


class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #1 sort
        for i in range(1,len(nums)):
            j = i
            temp = nums[j]
            while j>0 and temp<nums[j-1]:
                nums[j]=nums[j-1]
                j-=1

            nums[j]=temp

        #2check
        result=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                comp = target-nums[i]-nums[j]
                index = bisect.bisect_right(nums,comp,j+1)
                while index>j:
                  if index<len(nums) and (nums[i]+nums[j]+nums[index]<target):
                      result+=(index-j)
                  elif nums[i]+nums[j]+nums[index-1]<target :
                      result += (index - j-1)
                      break
                  else:
                      index-=1
        return result
'''
259. 3Sum Smaller
Medium
Given an array of n integers nums and an integer target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.



Example 1:

Input: nums = [-2,0,1,3], target = 2
Output: 2
Explanation: Because there are two triplets which sums are less than 2:
[-2,0,1]
[-2,0,3]
Example 2:

Input: nums = [], target = 0
Output: 0
Example 3:

Input: nums = [0], target = 0
Output: 0


Constraints:

n == nums.length
0 <= n <= 3500
-100 <= nums[i] <= 100
-100 <= target <= 100
'''