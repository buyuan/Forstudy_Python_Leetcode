class Solution:
    #1 divide and conquer, fail, hard to find the max from middle
    def D_C(self, nums:list[int], left: int, right:int):
        if left>=right:
            return nums[left]
        mid =int(left+ (right-left)/2)
        lMax = self.D_C(nums,0,mid-1)
        rMax = self.D_C(nums, mid+1, right)
        mMax = nums[mid]
        temp = mMax
        for i in range(mid-1,-1,-1):
            temp=temp*nums[i]
            mMax = max(mMax,temp)

        temp = mMax
        for i in range(mid+1,right+1):
            temp = temp * nums[i]
            mMax = max(mMax, temp)
        return max(rMax,max(mMax,lMax))

    def maxProduct(self, nums: list[int]) -> int:
        #max, min 是指到i index最大，最小乘积，其实是DP的思路，但是dp数组可以不用
        #三种情况，1）前面负数最小值，乘以当前负数，最大，2）前面正数最大，乘以当前正数，3）前面负数，当前正数，那么取当前
        Max = nums[0]
        Min = nums[0]
        res = nums[0]
        for i in range(1,len(nums)):
            temp = Max
            Max = max( max(Max*nums[i],Min*nums[i]), nums[i])
            Min = min( min(temp*nums[i],Min*nums[i]), nums[i])
            res = max(Max, res)
        return res

'''
152. Maximum Product Subarray
Medium
Given an integer array nums, find a
subarray
 that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.



Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
'''