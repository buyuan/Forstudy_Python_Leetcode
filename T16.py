import bisect
import sys

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        #1.sort
        for i in range (1,len(nums)):
            j=i
            temp = nums[j]
            while j>0 and temp<nums[j-1]:
                nums[j] = nums[j-1]
                j-=1
            nums[j] = temp
        #2 check,找到差异值在的位置(bisect function)，检查左右哪个更小，就用哪个
        result = sys.maxsize
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                comp = target-nums[i]-nums[j]
                right = bisect.bisect_right(nums,comp,j+1)
                left = right-1
                if right<len(nums) and abs(comp-nums[right])<abs(result):
                    result = comp-nums[right]
                if left >j and abs(comp-nums[left])<abs(result):
                    result = comp-nums[left]
            if result ==0:
               break
        return target - result


'''
16. 3Sum Closest
Medium
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.



Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0


Constraints:

3 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-104 <= target <= 104
'''