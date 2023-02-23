class Solution:
    def findPeakElement_linar(self, nums: list[int]) -> int:
        #局部峰值，只要比neighbord大就行,注意两个边界外都是极小值，比任何一个点都小
        #O(logn)的时间复杂度，肯定是二分法
        #1. 线性搜索，
        #如果是生序，那么第一个发现下降的地方， 肯定是局部峰，
        #如果是降序，一样，index=0就是峰
        #如果是波峰，那么找到满足下面条件的i时，i前面的元素都比i小，不然不可能走到i这一步
        for i in range(0,len(nums)-1):
            if nums[i]>nums[i+1]:
                return i
        return len(nums)-1

    def findPeakElement(self, nums: list[int]) -> int:
        #分三种情况，上升，下降，波峰，也是比较i和i+1
        #如果【i】<[i+1]那么是处于上升段，peak在右边，如果【i】>「i+1】，处于下降段，那么peak在左边
        #所以，二分法不断逼近，最后汇合的就是peak
        l,r = 0,len(nums)-1
        while(l<r):
            mid = l+int((r-l)/2)
            if nums[mid]>nums[mid+1]:
                #局部下降，说明peak在左边
                r = mid
            else:
                l=mid+1
        return l


'''
162. Find Peak Element
Medium
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.



Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.


Constraints:

1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
nums[i] != nums[i + 1] for all valid i.
'''