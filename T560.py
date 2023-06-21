class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        #用一个hashmap存从开头到当前出现过的某个和的次数，因为，如果到当前，值是X，那么，如果前面存在一个点，从开头到那个点的和是y。
        #使得 x-y =k,那么说明前面那个点到当前位置和为k，有几个这个样的点，就有几个自串和为k
        mp = {}
        #这个，0:1，是为了，当sum[x]刚好等于k时，为了符合相同的算法，x-y=k，需要一个y=0的值
        mp[0]=1
        sum,res=0,0
        for num in nums:
            sum+=num
            time = mp.get(sum-k)
            if  time:
                res+=time
            cur = mp.get(sum,0)
            mp[sum]=cur+1
        return res


'''
560. Subarray Sum Equals K
Medium
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107'''