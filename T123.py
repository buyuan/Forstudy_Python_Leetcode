import sys


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        #分治的思想，两次交易，那么可以是两次不重复的交易组合在一起（因为必须卖了才能买第二次，所以两次交易不会重合）
        #用两个数组，分别表示 left[i]是0到i的最大交易，right[i]是从i到n-1的最大交易，
        #遍历这两个数组，取一个i值，能够使得left[i]+right[i】最大
        left_buy,right_sell = prices[0],prices[-1]
        length = len(prices)
        pLeft = [0]*length
        pRight = [0]*length
        #第一个位置，都是0，因为同一天价格一样
        for i in range(1,length):
            #from left
            #0到i的左最大值要么i-1的最大值，要么是i点还在上升，到当前的最大值
            pLeft[i] = max(pLeft[i-1],prices[i]-left_buy)
            left_buy = min(left_buy, prices[i])

            #from right
            rIndex = length-i-1
            #从右到左，所以先找卖价，后找买价，
            pRight[rIndex] = max(pRight[rIndex+1],right_sell-prices[rIndex])
            # 用max，因为右边是先拿卖价，然后往前找买价，所以卖价要找大的
            right_sell = max(right_sell, prices[rIndex])
        ans = 0
        for i in range(length):
            ans = max(ans,pLeft[i]+pRight[i])

        return ans

'''
123. Best Time to Buy and Sell Stock III
Hard
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).



Example 1:

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.


Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 105
'''