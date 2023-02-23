class Solution:
    def canJump(self, nums: list[int]) -> bool:
        #DP, dp[i]意思是到达i点的剩余可跳的距离，所谓剩余可跳距离，例如，nums[3]=2.也就是说，3往前，最多可以两步，但是如果只有一步
        #则剩余的是1步（剩余只是一个概念，实际不会累加），另一方面，也可能是i=2的时候，原本可以走更多，但是没走
        #如果到某一点，剩余的步数小于0，则说明不能走到这一点
        dp = [0]*len(nums)
        for i in range(1,len(nums)):
            #减1是因为从i-1走到i，还需要一步
            temp = max(dp[i-1],nums[i-1])-1
            if temp<0:
                return False
            dp[i] = temp
        return True



'''
55. Jump Game
Medium
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.



Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.


Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105
'''