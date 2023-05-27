class Solution:
    def maximumProduct_better(self, nums: list[int]) -> int:
        #遍历一遍，找到最大的三个，最小的两个，然后计算，这就不用排序了
        max1,max2,max3,min1,min2 = -1001,-1001,-1001,1001,1001
        for n in nums:
            if n>max1:
                max1,max2,max3 = n,max1,max2
            elif n>max2:
                max2,max3 = n,max2
            elif n>max3:
                max3=n

            if n<min1:
                min1,min2=n,min1
            elif n<min2:
                min2=n
        return max(max1*max2*max3,min1*min2*max1)

    def maximumProduct(self, nums: list[int]) -> int:
        #生序排序，然后对比最后三个数字相乘，和前两个数字相乘最后一个数字，因为可能前两个是负数
        nums.sort()
        n = len(nums)-1
        if n<3:
            return nums[0]*nums[1]*nums[2]
        temp = nums[0]*nums[1]*nums[n]
        return max(temp, nums[n]*nums[n-1]*nums[n-2])
    

'''
628. Maximum Product of Three Numbers
Easy
3.7K
614
company
Microsoft
company
Amazon
company
Adobe
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

 

Example 1:

Input: nums = [1,2,3]
Output: 6
Example 2:

Input: nums = [1,2,3,4]
Output: 24
Example 3:

Input: nums = [-1,-2,-3]
Output: -6
 

Constraints:

3 <= nums.length <= 104
-1000 <= nums[i] <= 1000'''