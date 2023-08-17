class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        #这个方法很trick
        uni = set(nums)
        return (sum(uni)*3-sum(nums))//2

    #下面的算法，因为python最后一位是不是1，不一定是整数活着负数，所以计算会有错
    def singleNumber_fail2(self, nums: list[int]) -> int:
        bits=[0]*32
        n = len(nums)
        for num in nums:
            for i in range(n):
                bits[i]+=(num>>i)&1
        res=0
        for i in range(32):
            res |= (bits[i]%3)<<i
        return res

    def singleNumber_fail(self, nums: list[int]) -> int:
        #数字的某一个位，出现三次，那么除以三取余数，肯定是0，所以，每一位，加起来，除以三，余数就是只有一次的那个
        #用二进制，可以回避正负号的问题，因为最后一位用来表示正负，1是负，三个负数，除以三，余数就是0，被排除了
        res=0
        n = len(nums)
        for i in range(32):
            curDigit=0
            for j in range(n):
                #将数字的第i位右移到第一位，然后和1 与，就得到了这个数字的第一位
                curDigit+=(nums[j] >> i)&1
            #将获得的结果，除以三取余数，然后左移回原来的第i位，或运算想等于用位的和
            res |= (curDigit%3) << i
        return int(res)



'''
137. Single Number II
Medium
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,3,2]
Output: 3
Example 2:

Input: nums = [0,1,0,1,0,1,99]
Output: 99
 

Constraints:

1 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
Each element in nums appears exactly three times except for one element which appears once.'''