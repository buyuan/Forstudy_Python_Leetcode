class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        #DP,ways[i][j],表示，前i个数字，或加或减组成j的组合方式
        #ways[i+1][j+nums[i]]+=ways[i][j]
        #也就是说，例如当用3个元素构成和为5时候，如果第四个元素nums【4】=3,则，way[3][5]可以贡献一个way[4][7],即一个一个way[4][3]
        #就是j的+2，或者减2

        #首先计算出nums可以组成数据可能的范围，肯定是-sum到sum
        sum_ = sum(nums)
        if target>sum_ or target<-sum_:
            return 0
        #因为list是从0开始，所以，将原来的-sum到sum，移动sum，变成0，2sum
        offset = sum_
        length = len(nums)
        #从1开始，0,0是一个启动的条件
        ways= [[0]*(2*sum_+1) for i in range(length+1)]
        ways[0][offset]=1
        for i in range(length):
            for j in range(nums[i],2*sum_+1-nums[i]):
                #当用i的数字，j可能到达的范围是nums[i],即只用当前数字，到边界
                if ways[i][j]:
                    #就是way[i][j]可以贡献一个加一个数字，组合结果+-nums[i]
                    ways[i + 1][j + nums[i]] += ways[i][j]
                    ways[i + 1][j - nums[i]] += ways[i][j]
        return ways[length][target+offset]




    def findTargetSumWays_recursive(self, nums: list[int], target: int) -> int:
        #下面在这个方法超时了
        #递归，一正一负往后走
        res = [0]
        def helper(nums,target,start,res):
            if start>=len(nums):
                #走到头了
                if target==0:
                    #完成了目标任务
                    res[0]+=1
                return
            #下面一正一负继续往下走
            helper(nums, target - nums[start], start + 1, res)
            helper(nums, target + nums[start], start + 1, res)

        helper(nums, target, 0, res)
        return res[0]
'''     
494. Target Sum
Medium
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.



Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
Example 2:

Input: nums = [1], target = 1
Output: 1


Constraints:

1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000
'''