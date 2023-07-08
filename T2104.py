class Solution:
    def subArrayRanges(self, nums: list[int]) -> int:
        n=len(nums)
        res=0

        for i in range(n):
            #连续的子序列，实际就是固定左边，右边依次扩张，因此，扩张的过程中， 最大最小值可以一直计算出来
            #small，large是遍历过程中的最大最小值，
            small,large = nums[i],nums[i]
            for j in range(i+1,n):
                #这是从i到j的子序列
                small = min(small,nums[j])
                large = max(large,nums[j])
                res+=(large-small)
        return res

    #下面这个超时，需要优化下
    def subArrayRanges_O3(self, nums: list[int]) -> int:
        #求所有子序列
        res=0
        n=len(nums)
        for i in range(n):
            first = nums[i]
            for j in range(i,n):
                #这个子序列是从i到j，需要遍历这个list，找到最大最小值
                small,large = float('inf'), -float('inf')
                for k in range(i,j+1):
                    small = min(small,nums[k])
                    large = max(large,nums[k])
                res+=(large-small)
        return res

'''
2104. Sum of Subarray Ranges
Medium
You are given an integer array nums. The range of a subarray of nums is the difference between the largest and smallest element in the subarray.

Return the sum of all subarray ranges of nums.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,2,3]
Output: 4
Explanation: The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0 
[2], range = 2 - 2 = 0
[3], range = 3 - 3 = 0
[1,2], range = 2 - 1 = 1
[2,3], range = 3 - 2 = 1
[1,2,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.
Example 2:

Input: nums = [1,3,3]
Output: 4
Explanation: The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0
[3], range = 3 - 3 = 0
[3], range = 3 - 3 = 0
[1,3], range = 3 - 1 = 2
[3,3], range = 3 - 3 = 0
[1,3,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 2 + 0 + 2 = 4.
Example 3:

Input: nums = [4,-2,-3,4,1]
Output: 59
Explanation: The sum of all subarray ranges of nums is 59.
 

Constraints:

1 <= nums.length <= 1000
-109 <= nums[i] <= 109
'''