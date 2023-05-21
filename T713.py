class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        # 维护一个乘积小于k的滑动窗口，滑动窗口的宽度，刚好就是右边界为右边终点的结果的个数
        res,prdct,left=0,1,0
        for right in range(len(nums)):
            prdct*=nums[right]
            while left<=right and prdct>=k:
                prdct//=nums[left]
                left+=1
            res+=right-left+1
        return res

    def numSubarrayProductLessThanK_old(self, nums: list[int], k: int) -> int:
        #该方法超时
        res = 0
        for start in range(len(nums)):
            #在后面循环中统一用相乘，所以这个单独的元素单独处理
            end=start+1
            res_multi = nums[start]
            if nums[start]<k:
                res+=1
            while end<len(nums):
                res_multi *= nums[end]
                if res_multi<k:
                    res+=1
                else:break
                end+=1
        return res

'''
713. Subarray Product Less Than K
Medium
Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.



Example 1:

Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Example 2:

Input: nums = [1,2,3], k = 0
Output: 0


Constraints:

1 <= nums.length <= 3 * 104
1 <= nums[i] <= 1000
0 <= k <= 106
'''