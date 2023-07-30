class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        def numberLessOrEqual(x):
            #这个函数用来计算，两个数组的pair小于某一个值的个数,充分考虑数组的递增特性
            res=0
            j = len(nums2)-1
            for i in range(len(nums1)):
                while j>=0 and nums1[i]+nums2[j]>x:
                    j-=1
                res+=j+1
            return res
            
        #先找出第k小的和，然后两个数组遍历取出小于等于这个和的组合
        left,right = nums1[0]+nums2[0],nums1[-1]+nums2[-1]
        while left<right:
            mid =left+(right-left)//2
            count = numberLessOrEqual(mid)
            if count<k:
                #说明这个mid值小了，需要大一些，以容纳更多的pair
                left=mid+1
            else:
                #继续往左逼近，找到最小的一个值，保证小于这个值的组合等于k
                right=mid
        #这个tar最终一定是两个数组的一个pair值，因为二分查找的+1，保证了是间距为1的速度逼近，所以一定能找到第k小的值
        tar = left

        #开始求和小于tar的pair
        res=[]
        for i in range(len(nums1)):
            j=0
            while j<len(nums2) and nums1[i]+nums2[j]<tar:
                res.append([nums1[i],nums2[j]])
                j+=1
        #如果不够k个，继续求等于tar的pair
        for i in range(len(nums1)):
            j=0
            while j<len(nums2) and nums1[i]+nums2[j]<=tar and len(res)<k:
                #在里面判断相等， 不然循环不起来
                if nums1[i]+nums2[j]==tar:
                    res.append([nums1[i],nums2[j]])
                j+=1
        return res

'''
373. Find K Pairs with Smallest Sums
Medium
5.7K
356

You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

 

Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
Example 3:

Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [[1,3],[2,3]]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]
 

Constraints:

1 <= nums1.length, nums2.length <= 105
-109 <= nums1[i], nums2[i] <= 109
nums1 and nums2 both are sorted in non-decreasing order.
1 <= k <= 104'''