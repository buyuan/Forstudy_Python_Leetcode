class Solution:
    def maxProfit(self, k: int, prices:  list[int]) -> int:
        #hold表示手上还有股票，hold[k】表示，我买卖了k次，手上还有，再卖就是k+1次
        #sold表示手上没有股票了， sole[k]表示，买卖了k次，在hold[k]基础上再卖，就是sold[k+1]
        #用-2000是因为，题目的price最高是1000，所以hold的最小值不会小于1000
        #取之范围是0，什么也没干，到k，买卖k次
        hold,sold = [-2000]*(k+1),[0]*(k+1)
        hold[0]=-prices[0]
        for i in range(1, len(prices)):
            #每一次循环实际就是每天之后的可能的状态
            
            #第i天hold[0]的状态是指，什么也没发生或者当天买了一次
            hold[0] = max(hold[0],-prices[i])
            for j in range(1,k+1):
                #k种状态
                #啥也不干，或者我卖了j次，然后再买，注意，hold[j]是卖了j次，然后再买，不买出，因为完整的卖出才是下一次
                hold[j] = max(hold[j],sold[j]-prices[i])
                 #啥也不干，或者卖了j-1次之后，手上还有股票， 把它卖了
                sold[j] = max(sold[j],hold[j-1]+prices[i])
        return max(sold)

'''
188. Best Time to Buy and Sell Stock IV
Hard
6.9K
201
You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions: i.e. you may buy at most k times and sell at most k times.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
 

Constraints:

1 <= k <= 100
1 <= prices.length <= 1000
0 <= prices[i] <= 1000
'''