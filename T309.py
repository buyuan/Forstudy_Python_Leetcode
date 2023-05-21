class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        #维护三个数组，买，卖，停
        n = len(prices)
        sell,buy,cool = [0]*n,[0]*n,[0]*n
        buy[0] = -prices[0]
        for i in range(1,n):
            #我第I天能卖的最大收益， 要么就是上一天卖的收益，要么就是上一天买了， 今天卖
            sell[i] = max(sell[i-1],buy[i-1]+prices[i])
            #第i天买的最大收益，要么就是上一天，（这一天没买），或者昨天休息了，今天卖
            buy[i]  = max(buy[i-1],cool[i-1]-prices[i])
            #i天休息，能得到的最大汇总利益是
            cool[i] = max(cool[i-1], max(buy[i-1],sell[i-1]))
        #最后一天卖出，收益肯定最大
        return sell[n-1]

'''
309. Best Time to Buy and Sell Stock with Cooldown
Medium

You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).



Example 1:

Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
Example 2:

Input: prices = [1]
Output: 0


Constraints:

1 <= prices.length <= 5000
0 <= prices[i] <= 1000
'''