class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        #1 前n-k的数字翻转（逆序）
        left=0
        right = len(nums)-k-1
        while(left<right):
            cur = nums[left]
            nums[left] = nums[right]
            nums[right]=cur
            left+=1
            right-=1
        #2 后 k个数字翻转
        left = len(nums)-k
        right = len(nums) - 1
        while (left < right):
            cur = nums[left]
            nums[left] = nums[right]
            nums[right] = cur
            left += 1
            right -= 1
        #3整体翻转
        left =0
        right = len(nums) - 1
        while (left < right):
            cur = nums[left]
            nums[left] = nums[right]
            nums[right] = cur
            left += 1
            right -= 1

    def rotate_old(self, nums: list[int], k: int) -> None:
        #每次前移动1，k就执行k轮
        #超时
        if len(nums) <=1:
            return
        for j in range(0,k):
            cur = nums[0]
            for i in range(len(nums)-1,-1,-1):
                index = (i+1)%len(nums)
                nums[index] = nums[i]
            nums[1] = cur



'''
189. Rotate Array
Medium
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]


Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
'''