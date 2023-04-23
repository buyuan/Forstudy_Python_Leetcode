import sys


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        #m,n两个数组，中间的位置是k=（m+n+1）/2， 如果第一个数字去x1个数字，第二个取x2个数字，
        #则x1+x2=K，对于偶数，中位数是，（nums[k]+nums[k-1])/2,对于奇数，就是nums[k](nums[k]指合并两个数组后的第k个
        #！！对于nums[k-1]，必然是num1[x1-1]，nums2[x2-1]之间大的那个，对于nums[k]，必定是nums1[x1]，nums2[x2]之间小的那个
        #关系一定是 nums1[x1]大于nums2[x2-1],因为 num1[x1],nums2[x2]的较小者的左边是num1[x1-1],nums2[x2-1]的较大者
        #以此关系建立二分搜索
        n1,n2 = len(nums1),len(nums2)
        if n1>n2:
            #用短的处理，减少循环次数
            return self.findMedianSortedArrays(nums2,nums1)
        l,r=0,n1
        k = (n1+n2+1)//2
        while l<r:
            x1 = l+(r-l)//2
            x2 = k-x1
            if nums1[x1]<nums2[x2-1]:
                #说明nums1用的数字少了，因为需要更大的nums1[mid]，或者更小的nums2【x2-1】
                l=x1+1
            else:
                #这种情况，就是尝试是否可以有更小范围的nums1使用，一直要找到边界
                r=x1
        #出来一个l=r,这个l就是nums1使用的数字个数
        x1,x2 = l,k-l
        #大于0才说明用到了，可以参加对比，否则是根本没用到
        midL = max(nums1[x1-1] if x1>0 else -sys.maxsize-1,nums2[x2-1] if x2>0 else -sys.maxsize-1)

        if (n1+n2)%2==1:
            #odd
            return midL
        #如果x超过了,说明这个数组全用完了，所以结果不会在这个数组
        midR = min(nums1[x1] if x1<n1 else sys.maxsize, nums2[x2] if x2<n2 else sys.maxsize)
        return (midL+midR)/2


'''
4. Median of Two Sorted Arrays
Hard
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
Constraints:
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
'''