class Solution:
    #下面这个方法，超时，测试case会有一个巨大的数组
    def largestRectangleArea_old(self, heights: list[int]) -> int:
        # 找局部峰值，即该节点比后面节点大 因为，这样的节点，能容纳前面的节点组成，
        # 找到后从前遍历到该节点，计算一个矩形大小，找最大一个局部峰值形成的矩形
        res = 0
        length = len(heights)
        for i in range(length):
            if i + 1 < length and heights[i] <=heights[i + 1]:continue
                #只要不是峰值都不要，不能用heights[i] >heights[i + 1]，因为可能漏掉最后一个是峰值的情况
            # 局部峰值
            minHeight = heights[i]
            for j in range(i, -1, -1):
                # 从局部峰值开始往前遍历，找这个局部峰值为终点的最大矩形面积
                minHeight = min(minHeight, heights[j])
                area = minHeight * (i-j + 1)
                res = max(res, area)
        return res

    def largestRectangleArea(self, heights: list[int]) -> int:
        #这个方法和上面思路相似， 就是维护一个递增的栈，当下一个数变小时，开始计算面积
        #计算的方法也是依次往前遍历
        #放0是为了触发到结尾时，要计算一下面积，以免最后一个数字是生序，无法计算
        heights.append(0)
        stk=[]
        res = 0
        starIndex = 0
        for i in range(len(heights)):
            if not stk:
                starIndex=i
            while stk and heights[i]<heights[stk[-1]]:
                curIndex = stk.pop()
                area = 0
                if not stk:
                    area = heights[curIndex]*(i-starIndex)
                else:
                    area = heights[curIndex]*(i-stk[-1]-1)
                res = max(res,area)
            stk.append(i)
        return res


'''
84. Largest Rectangle in Histogram
Hard
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:
Input: heights = [2,4]
Output: 4
Constraints:
1 <= heights.length <= 105
0 <= heights[i] <= 104
'''