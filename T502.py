import heapq


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        #思路就是，要找到可以执行的project中的最大的收益，那么，capital按照最小的排序，每次对比w，找到可以执行的项目
        #同时，对这些capital对应的profit排序，每次找最大的profit

        maxProfit= [] #maxProfit that can afford
        minCapital = [(c,p) for c,p in zip(capital,profits)]
        #最小堆，堆顶是最小的capital，默认用第一个排序
        heapq.heapify(minCapital)
        while k>0:
            #找k次
            k-=1
            while minCapital and minCapital[0][0]<=w:
                #还有项目可选，以及最小的capital的项目可用，就可以继续，
                c, p = heapq.heappop(minCapital)
                #实际上因为w是一直累加的，所以加入maxProfit的项目一直都可以选，而随着w增大，更多capital大的项目可以加入
                #profit都是正数，所以用最小堆，存相反数
                heapq.heappush(maxProfit,-p)

            #出来之后，堆顶是最大profit
            if maxProfit: w+= -heapq.heappop(maxProfit)
        return w


'''
502. IPO
Hard
Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited resources, it can only finish at most k distinct projects before the IPO. Help LeetCode design the best way to maximize its total capital after finishing at most k distinct projects.

You are given n projects where the ith project has a pure profit profits[i] and a minimum capital of capital[i] is needed to start it.

Initially, you have w capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.

Pick a list of at most k distinct projects from given projects to maximize your final capital, and return the final maximized capital.

The answer is guaranteed to fit in a 32-bit signed integer.

 

Example 1:

Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
Output: 4
Explanation: Since your initial capital is 0, you can only start the project indexed 0.
After finishing it you will obtain profit 1 and your capital becomes 1.
With capital 1, you can either start the project indexed 1 or the project indexed 2.
Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.
Example 2:

Input: k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
Output: 6
 

Constraints:

1 <= k <= 105
0 <= w <= 109
n == profits.length
n == capital.length
1 <= n <= 105
0 <= profits[i] <= 104
0 <= capital[i] <= 109'''