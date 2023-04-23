class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        #用set，找到一个数字，前后寻找连续的，找到了就删除，以便减少后续数字的遍历
        st = set()
        for num in nums:
            st.add(num)
        back,forward,count = -1,1,1

        ans = 0
        for num in nums:
            if not st.__contains__(num):
                continue
            st.remove(num)
            while st.__contains__(num+back):
                st.remove(num + back)
                back-=1
                count+=1
            while st.__contains__(num+forward):
                st.remove(num+forward)
                forward+=1
                count += 1
            ans = max(ans,count)
            back,forward,count = -1,1,1
        return ans
'''
128. Longest Consecutive Sequence
Medium
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.



Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9


Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
'''