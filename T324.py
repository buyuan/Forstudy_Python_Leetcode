import copy


class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums i   n-place instead.
        """
        #因为是严格大于，小于，所以要保证两个数是尽量隔开的，不能是连续两个数交换了。
        temp = copy.deepcopy(nums)
        temp.sort()
        mid = int((len(temp)-1)/2)
        right = len(temp)-1
        for i in range(0,len(nums)):
            if i%2==0:
                #小
                nums[i] = temp[mid]
                mid-=1
            else:
                #大
                nums[i] = temp[right]
                right -= 1

'''
324. Wiggle Sort II
Medium
2.6K
885
company
Amazon
company
Microsoft
company
Google
Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

You may assume the input array always has a valid answer.



Example 1:

Input: nums = [1,5,1,1,6,4]
Output: [1,6,1,5,1,4]
Explanation: [1,4,1,5,1,6] is also accepted.
Example 2:

Input: nums = [1,3,2,2,3,1]
Output: [2,3,1,3,1,2]


Constraints:

1 <= nums.length <= 5 * 104
0 <= nums[i] <= 5000
It is guaranteed that there will be an answer for the given input nums.

'''