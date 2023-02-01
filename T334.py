import math


class Solution:
    #下面这个超时
    def increasingTriplet_DP(self, nums: list[int]) -> bool:
        # 用dp，dp[i]表示0-i范围内，小于等于nums【i】的数的个数
        dp = [1]*len(nums)
        for i in range(0,len(nums)):
            j = 0
            while(j<i):
                if nums[j]<nums[i]:
                    #下面这部分是关键，如果dp[j]==2,说明dp[j]已经是两个数字的连续递增，此时到i正好是第三个
                    dp[i] = max(dp[i],dp[j]+1)
                    if dp[i]>=3:
                        return True
                j+=1
        return False

    # 2 建立两个数组，前，后，分别表示，0～i的最小值， i~n-1最大值，然后在遍历这两个数组，如果存在 前[i]<nums[i]<后【i】
    #则说明，在i，存在一个递增
    def increasingTriplet_2arr(self, nums: list[int]) -> bool:
        length = len(nums)
        small = [nums[0]]*length
        large = [nums[length-1]]*length
        for i in range(1,len(nums)):
            for j in range(1,i):
                # 0~i
                small[j] = min(small[j-1],nums[j])
            for k in range(length-2,i-1,-1):
                # length-1~i
                large[k] = max(large[k+1],nums[k])
        for j in range(0,length):
            if nums[j]>small[j] and nums[j]<large[j]:
                return True
        return False

    #3 上面那个超时，同样的思路可以换一种写法，利用上一个值来算，有点dp思路，即，我上一个已经是极值，当前值大或者小，都能判断是不是极值,不用再从头搜一遍
    def increasingTriplet(self, nums: list[int]) -> bool:
        length = len(nums)
        forwardSmall = [nums[0]] * length
        backwardLarge = [nums[length - 1]] * length
        for i in range(1,length):
            forwardSmall[i] = min(forwardSmall[i-1],nums[i])
        for i in range(length-2,-1,-1):
            backwardLarge[i] = max(backwardLarge[i+1],nums[i])
        for i in range(0,length):
            if nums[i]>forwardSmall[i] and nums[i]<backwardLarge[i]:
                return True
        return False
'''
334. Increasing Triplet Subsequence
Medium
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.
Example 1:
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.


Constraints:

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1

'''