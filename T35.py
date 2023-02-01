class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums)
        while(left<right):
            mid = left+int((right-left)/2)
            if nums[mid]==target:
                return mid
            if nums[mid]<target:
                left=mid+1
            else :
                #包含了相等
                right=mid
        return right

'''
35. Search Insert Position
Easy
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
'''