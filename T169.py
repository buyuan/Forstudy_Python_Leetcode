class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        dic = {}
        length = len(nums)
        for num in nums:
            count = dic.get(num,0)
            count += 1
            if count >int(length/2):
                return num
            dic[num] = count

    #下面这个挺巧秒
    def majorityElement_2(self, nums: list[int]) -> int:
        return sorted(nums)[int(len(nums) / 2)]
'''
169. Majority Element
Easy
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
Example 1:
Input: nums = [3,2,3]
Output: 3
Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
Constraints:
n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
'''