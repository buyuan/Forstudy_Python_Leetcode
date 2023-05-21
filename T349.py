class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        #遍历一个数组，在另一个数组中找看能不能找到
        nums1.sort()
        st = set()
        for num in nums2:
            l,r = 0,len(nums1)
            while l<r:
                mid = l+(r-l)//2
                if num==nums1[mid]:
                    st.add(num)
                    break
                if nums1[mid]<num:
                    l=mid+1
                else:
                    r=mid
        return list(st)
'''
349. Intersection of Two Arrays
Easy

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.



Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.


Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000

'''