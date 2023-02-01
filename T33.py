class Solution:
    '''
        旋转可以导致数组分为两个区域，上半区，下半区，都是分别递增的 ，其中，下半区的最大值（右端点）小于上半区的最小值（左端点）
        二分法的目的，就是保证搜索的值，一直在左右端点之间
    '''
    def search(self, nums: list[int], target: int) -> int:
        if not nums or len(nums)==0:
            return -1
        left =0
        right = len(nums)-1
        #while(left<=right): 用这个条件，会导致死循环，因为left。right会相等，我代码中取值都是带等号，很容易边界重合

        while(left+1<right):
            mid = left+int((right-left)/2)
            if nums[mid] == target:
                return mid
            if nums[mid]>=nums[left]:
                #上半区
                if nums[mid]>=target and nums[left]<=target:
                    #上，左
                    right = mid
                else:
                    #  上右
                    left = mid
            else:
                #下半区
                if target<=nums[right] and target>=nums[mid]:
                    #下 右
                    left = mid
                else:
                    #下左
                    right = mid

        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1
'''
33. Search in Rotated Sorted Array
Medium
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1


Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
'''