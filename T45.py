class Solution:
    def jump_dp(self, nums: list[int]) -> int: 
        #dp[i]是指到达i点的最小次数

        #最差的情况，每次只能一步，所以dp[i]=i
        dp = [ i for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(1,nums[i]+1):
                #对于每一个点，计算一个往后走的所有可能中的最小值
                if i+j>=len(nums):break #不需要走到超过边界
                #从i到j的最小次数，要么是其他地方计算的dp[i+j],要么就是dp[i]一步过去
                dp[i+j] = min(dp[i+j],dp[i]+1)
        return dp[-1]

    def jump(self, nums: list[int]) -> int:
        #每次跳之前，确定这次跳可以到达的最大位置，以及这之间的点，可以决定下次跳的最大位置
        #注意，这个不是greedy，而是我每次跳跃前，都确定我可能的跳跃的最大范围，以及这个范围内，我可能的下次跳跃的最大范围
        res =0
        curEnd,curFarest=0,0
        for i in range(len(nums)-1):
            #只用遍历到-2的位置，一方面题目保证有解，另一方面，遍历到最后，逻辑有+=1，所以都会多出1了
            #确定在当前的curEnd范围内，可能走到的下次的end最大位置
            curFarest = max(curFarest,i+nums[i])

            if i==curEnd:
                #扫描完这次跳跃的可达到的范围，需要跳了
                res+=1
                #将这次跳之后可能达到的最远位置，作为下次扫描的范围
                curEnd=curFarest
        return res


'''
45. Jump Game II
Medium
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].'''