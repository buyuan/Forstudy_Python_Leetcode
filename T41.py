class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        #用一个set,然后把正数放进去，再从1开始，看set中哪个没有就返回哪个
        st = set()
        for num in nums:
            if num>0:
                st.add(num)
        ans=1
        for val in st:
            if st.__contains__(ans):
                ans+=1
                continue
            return ans
        return ans
'''
41. First Missing Positive
Hard

Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.



Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.


Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
'''