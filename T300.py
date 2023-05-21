class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        #dp,dp[i[表示前i个数里面最大的连续数字个数
        #关系共识  dp[i]=max(dp[i].dp[j]+1), dp[j]是i之前的位置，当num[i]>num[j]的时候，dp[j]+1刚好能延长一个长度
        dp = [1]*len(nums)
        res = 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)
            res = max(res,dp[i])
        return res
'''
300. Longest Increasing Subsequence
Medium
Given an integer array nums, return the length of the longest strictly increasing
subsequence
.



Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1


Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104



'''