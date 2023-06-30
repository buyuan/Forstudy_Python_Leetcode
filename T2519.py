import heapq


class Solution:
    def kBigIndices(self, nums: list[int], k: int) -> int:
        #用heap自动排序的特点，在遍历nums的时候，可以轻松知道nums[i]之前，是不是有k个数字小于nums[i]
        def helper(nums,k):
            #返回一个数组，标记哪个下标的左边有不小于k个数字小雨nums[i]
            size = len(nums)
            res = [0]*size
            hp=[]
            for i in range(size):
                #对于heapq，处理一个list之后，只能保证第一个是最小的数字，并不是让原来的list排序，所以，
                #要放入-nums[i],变成实际的最大堆，都是正数，所以可以通过放负数处理
                if len(hp)<k:
                    heapq.heappush(hp,-nums[i])
                    continue
                
                if nums[i]>-hp[0]:
                    #nums[i]之前有k个小的数字，满足要求
                    res[i]=1
                #满k个之后，要做的，就是push之后，把最大的pop出来，这样能保证hp里面的k的是最小的k个
                heapq.heappushpop(hp,-nums[i])
            return res
        left = helper(nums,k)
        #nums[i]右边的个数就是反转nums之后，左边的个数，这个坐标实际上是逆序的，所以需要再逆序回来
        right = helper(nums[::-1],k)[::-1]
        ans=0
        for i in range(len(nums)):
            if left[i] and right[i]:
                #左右两边都满足的
                ans+=1
        return ans
'''
2519. Count the Number of K-Big Indices
Hard
You are given a 0-indexed integer array nums and a positive integer k.

We call an index i k-big if the following conditions are satisfied:

There exist at least k different indices idx1 such that idx1 < i and nums[idx1] < nums[i].
There exist at least k different indices idx2 such that idx2 > i and nums[idx2] < nums[i].
Return the number of k-big indices.

 

Example 1:

Input: nums = [2,3,6,5,2,3], k = 2
Output: 2
Explanation: There are only two 2-big indices in nums:
- i = 2 --> There are two valid idx1: 0 and 1. There are three valid idx2: 2, 3, and 4.
- i = 3 --> There are two valid idx1: 0 and 1. There are two valid idx2: 3 and 4.
Example 2:

Input: nums = [1,1,1], k = 3
Output: 0
Explanation: There are no 3-big indices in nums.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i], k <= nums.length'''