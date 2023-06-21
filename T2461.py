class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        sum=0
        res=0
        #用set似乎删除内容很慢，该用hashmap
        dct={}
        for i in range(len(nums)):
            if dct.get(nums[i]):
                dct[nums[i]]+=1
            else:
                dct[nums[i]]=1
            sum+=nums[i]
            
            if i>=k:
                #要开始移动了
                dct[nums[i-k]]-=1
                if dct.get(nums[i-k])==0:
                    del dct[nums[i-k]]
                sum-=nums[i-k]
            #下面这个放在上一步之后，因为移动后，先去掉前一个，在看新的窗口内的大小
            if i>=k-1:
                #每次判断新的框是否全是不重复的，然后确定是否要这个sum
                if len(dct)==k:
                    res = max(res,sum)
        return res


'''
2461. Maximum Sum of Distinct Subarrays With Length K
Medium
You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:

The length of the subarray is k, and
All the elements of the subarray are distinct.
Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,5,4,2,9,9,9], k = 3
Output: 15
Explanation: The subarrays of nums with length 3 are:
- [1,5,4] which meets the requirements and has a sum of 10.
- [5,4,2] which meets the requirements and has a sum of 11.
- [4,2,9] which meets the requirements and has a sum of 15.
- [2,9,9] which does not meet the requirements because the element 9 is repeated.
- [9,9,9] which does not meet the requirements because the element 9 is repeated.
We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions
Example 2:

Input: nums = [4,4,4], k = 3
Output: 0
Explanation: The subarrays of nums with length 3 are:
- [4,4,4] which does not meet the requirements because the element 4 is repeated.
We return 0 because no subarrays meet the conditions.
 

Constraints:

1 <= k <= nums.length <= 105
1 <= nums[i] <= 105'''