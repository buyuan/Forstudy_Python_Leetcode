class Solution:
    #小大，小大，。。。 先排序，然后从第三个数开始，每一组（两个）互相交换
    def wiggleSort(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # sorted返回一个新的列表，不改变原来list
        #nums = sorted(nums)
        # sort直接改变原职
        nums.sort()
        for i in range(2, len(nums), 2):
            nums[i],nums[i-1] = nums[i-1],nums[i]
        if None:
            pass
'''
280. Wiggle Sort
Medium
Given an integer array nums, reorder it such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

You may assume the input array always has a valid answer.



Example 1:

Input: nums = [3,5,2,1,6,4]
Output: [3,5,1,6,2,4]
Explanation: [1,6,2,5,3,4] is also accepted.
Example 2:

Input: nums = [6,6,5,6,3,8]
Output: [6,6,5,6,3,8]


Constraints:

1 <= nums.length <= 5 * 104
0 <= nums[i] <= 104
It is guaranteed that there will be an answer for the given input nums.
'''