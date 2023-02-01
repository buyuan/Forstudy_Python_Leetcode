class Solution:
    #dp, dp[i]是指，index i结尾的子数组的最大的和
    def maxSubArray(self, nums: list[int]) -> int:
        res = nums[0]
        dp = [None]*len(nums)
        dp[0] = nums[0]
        for i in range(1,len(nums)):
            last = 0 if dp[i-1]<0 else dp[i-1]
            dp[i] = nums[i]+ last
            res = max(res,dp[i])
        return res

    #divide & conquer
    #left most, right most, mid most,
    def D_C(self,nums: list[int], left:int, right:int):
        if left>=right:
            return nums[left]
        mid = int(left+ (right-left)/2)
        lMax = self.D_C(nums,left,mid-1)
        rMax = self.D_C(nums,mid+1,right)
        mMax = nums[mid]
        temp = mMax
        for i in range(mid-1,-1,-1):
            temp=temp+nums[i]
            mMax = max(temp,mMax)
        temp = mMax
        for i in range(mid+1,right+1):
            temp = temp+nums[i]
            mMax = max(temp,mMax)
        return max(lMax,max(rMax,mMax))

    def maxSubArray_2(self, nums: list[int]) -> int:
        return self.D_C(nums,0,len(nums)-1)
'''
53. Maximum Subarray
Medium
Given an integer array nums, find the
subarray
 with the largest sum, and return its sum.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
'''