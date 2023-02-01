class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        #尝试一下找到一个，然后前后找一下
        left,right=0,len(nums)-1
        index=-1
        while(left<=right):
            mid = left+int((right-left)/2)
            if nums[mid] == target:
                index = mid
                break
            if nums[mid]<target:
                left = mid+1
            else:
                right=mid-1
        if index ==-1:
            return [-1,-1]
        l,r = index,index
        while True:
            if l>0 and nums[l-1]==target:
                l-=1
            else:
                break
        while True:
            if r<len(nums)-1 and nums[r+1]==target:
                r+=1
            else:
                break
        return [l,r]


'''
34. Find First and Last Position of Element in Sorted Array
Medium
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]


Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
'''