import sys


class Solution:
    #下面这个超时
    def maxProfit_old(self, prices: list[int]) -> int:
        #最简单的方式，bruce force，双循环
        ans = 0
        for i in range(len(prices)-1):
            for j in range(i+1,len(prices)):
                ans = max(ans,prices[j]-prices[i])
        return ans

    def maxProfit(self, prices: list[int]) -> int:
        #两个变量，一个记录最小买价，另一个记录差价，因为是一直往后走，所以不用担心越过可能的答案
        #例如，1， 最小值在一开始，则后面的新的值不会用来计算差价，
        #例如，2. 最小值在后面，则如果最大差值在前面，则不会有影响，如果最大差值在后面，则正常计算出来
        ans,buy = 0,sys.maxsize
        for price in prices:
            buy = min(buy,price)
            ans = max(ans,price-buy)
        return ans

'''
121. Best Time to Buy and Sell Stock
Easy
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
'''