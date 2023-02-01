import math


class Solution:
    # this O(n^2), will excess time limit
    def maxSubArrayLen_old(self, nums: list[int], k: int) -> int:
        ans = 0
        temp = k
        for i in range(0, len(nums)):
            temp = temp-nums[i]
            if temp == 0:
                ans =max(ans,1 )
            for j in range(i+1, len(nums)):
                temp = temp - nums[j]
                if temp == 0:
                    ans = max(j-i+1, ans)
                    #temp = k
            temp = k
        return ans
    '''
    建立累计数组，即，sum[j]是前j项的和，则找到k，相当于找一下，当便利到j
    时候，是否在j之前存在一个index，使得，sum[j]-sum[index]=k,如果存在， 则j到index的距离就是答案
    因此，需要一个map，key是前n项和，value是n这个index，
    同时，因为从0到j本身也可能是个答案，而从累计到坐标j的距离为j+1，所以，0这个value的坐标为-1，因此能够使得
    当sum【j】=k时，j-（-1）就是答案，同时，这个map建立的过程中，如果相同的key存在则不再修改，因为要取最长，所以，越早
    出现的，会和后面距离越长
    '''
    def maxSubArrayLen(self, nums: list[int], k: int) -> int:
        # accumulation list
        accSum = [math.inf]*len(nums)
        accSum[0]=nums[0]
        # value,index map
        accMap = { }
        accMap[0] = -1
        if not accMap.__contains__(accSum[0]):
            #in case map[0] is 0
            accMap[accSum[0]] = 0
        for i in range(1, len(nums)):
            accSum[i] =accSum[i-1]+nums[i]
            if not accMap.__contains__(accSum[i]):
                accMap[accSum[i]]=i

        ans = 0
        for i in range(0,len(accSum)):
            if accMap.__contains__(accSum[i]-k):
                ans = max(ans,i-accMap[accSum[i]-k])
        return ans



'''
325. Maximum Size Subarray Sum Equals k
Medium
Given an integer array nums and an integer k, return the maximum length of a
subarray
 that sums to k. If there is not one, return 0 instead.
Example 1:

Input: nums = [1,-1,5,-2,3], k = 3
Output: 4
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
Example 2:

Input: nums = [-2,-1,2,1], k = 1
Output: 2
Explanation: The subarray [-1, 2] sums to 1 and is the longest.


Constraints:

1 <= nums.length <= 2 * 105
-104 <= nums[i] <= 104
-109 <= k <= 109

'''