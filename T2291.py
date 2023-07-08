class Solution:
    def minCost(self, nums: list[int], costs: list[int]) -> int:
        #dp+monotonic stack
        #dp[i]是指，跳到第i 个index，最小的代价,无论是从哪个点跳到i
        #另外，注意审题，costs[i]是指，无论从哪里跳到i都要花的代价，这个题的重点是找到那些点可以往i跳
        '''
        用单调栈，比如单调递减栈，是指从i往左看的单调递减栈，栈顶
        是往左看第一个小于等于i对应的值，first left<=right,则有可能符合第一种场景
        在维护单调递减栈的过程中，发现一个大的元素，然后弹出的过程，都是在弹出比当前i的值小，同时弹出的数字又比左边更小，是完全符合第一种场景的
        所以，这些弹出的值，都可以作为跳的起点。
        同时，如果递减栈不符合条件，用递增栈，原理一样。
        目的都是为了找从某个点跳到i的最小代价
        注意理解，单调栈建立过程的处理，而不是说处理完的结果
        '''
        dp = [float('inf')]* len(nums)
        dp[0]=0
        stk_desc,stk_asc = [],[] #记录的是从i往左边看的节点，但是实际也是一个从左往右维护的过程

        for i in range(len(nums)):
            while stk_desc and nums[i]>=nums[stk_desc[-1]]:
                #如果发现这个值是大值，往前找小值条
                dp[i] = min(dp[i],dp[stk_desc.pop()]+costs[i])
            while stk_asc and nums[i]<nums[stk_asc[-1]]:
                dp[i] = min(dp[i],dp[stk_asc.pop()]+costs[i])
            stk_desc.append(i)
            stk_asc.append(i)
        return dp[-1]

'''
2297. Jump Game VIII
Medium
You are given a 0-indexed integer array nums of length n. You are initially standing at index 0. You can jump from index i to index j where i < j if:

nums[i] <= nums[j] and nums[k] < nums[i] for all indexes k in the range i < k < j, or
nums[i] > nums[j] and nums[k] >= nums[i] for all indexes k in the range i < k < j.
You are also given an integer array costs of length n where costs[i] denotes the cost of jumping to index i.

Return the minimum cost to jump to the index n - 1.

 

Example 1:

Input: nums = [3,2,4,4,1], costs = [3,7,6,4,2]
Output: 8
Explanation: You start at index 0.
- Jump to index 2 with a cost of costs[2] = 6.
- Jump to index 4 with a cost of costs[4] = 2.
The total cost is 8. It can be proven that 8 is the minimum cost needed.
Two other possible paths are from index 0 -> 1 -> 4 and index 0 -> 2 -> 3 -> 4.
These have a total cost of 9 and 12, respectively.
Example 2:

Input: nums = [0,1,2], costs = [1,1,1]
Output: 2
Explanation: Start at index 0.
- Jump to index 1 with a cost of costs[1] = 1.
- Jump to index 2 with a cost of costs[2] = 1.
The total cost is 2. Note that you cannot jump directly from index 0 to index 2 because nums[0] <= nums[1].
 

Constraints:

n == nums.length == costs.length
1 <= n <= 105
0 <= nums[i], costs[i] <= 105'''