class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        #先算总的积，再除以当前index的值，
        #在累乘的过程中，如果遇到0，则跳过，且把结果积的其他值置零
        #如果遇到两个0，则全置零
        ans = [0]*len(nums)
        zeroIndex=-1
        totalPro = 1
        for i in range(0, len(nums)):
            if nums[i]==0:
                if zeroIndex!=-1:
                    #发现两个0,则数组全0
                    return ans
                zeroIndex =i
                continue
            totalPro *=nums[i]
        if zeroIndex != -1:
            ans[zeroIndex] = totalPro
            return ans

        for i in range(0,len(nums)):
            ans[i] = int(totalPro/nums[i])
        return ans
'''
238. Product of Array Except Self
Medium
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.



Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
'''