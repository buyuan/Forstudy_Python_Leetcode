class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        #dp[i]是指，金额为i时候，最少需要几个硬币，于是，推导公式变成
        #dp[i] = min(dp[i],dp[i-coin[j]]+1),例如我是11，我可以用6元钱时候最小个数，+一个5元就可以
        #初始化为amount+1，就是说比全1元硬币还要多一个1
        dp = [amount+1]*(amount+1)
        dp[0]=0
        for i in range(1,amount+1):
            for coin in coins:
                if coin<=i:
                    dp[i] = min(dp[i],dp[i-coin]+1)
        return dp[amount] if dp[amount]<=amount else -1
'''
322. Coin Change
Medium
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.



Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0


Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
'''