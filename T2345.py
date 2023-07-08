from collections import Counter, defaultdict


class Solution:

    #下面这个算法过不了 [[2,2],[2,2],[3,1]] 这个case，因为会把完全相同的都去掉，但是这三个世纪都不算看到
    def visibleMountains(self, peaks: list[list[int]]) -> int:
        #用底边（x轴上面的斜边）做合并，或者类似于做差集，或者重复的地方融合，有不交叉的就说明可见
        #1 将peak转化为底边范围，并且需要去掉完全相同的部分
        allEdges=[]
        for x,y in peaks:
            #先转换为底边
            allEdges.append((x-y,x+y))
        #去掉完全包在里面的，但保留相同的，相同的下一步再去掉
        allEdges.sort(key = lambda x : (x[0],-x[1]))
        l,r = allEdges[0][0],allEdges[0][1]
        preEdges = []
        preEdges.append((l,r))
        for i in range(1,len(allEdges)):
            a,b = allEdges[i][0],allEdges[i][1]
            if a>=l and b<=r:
                if a==l and b==r:
                    #保留完全相同的放在下一次去掉
                    preEdges.append((a,b))
                else:
                    continue
            else:
                preEdges.append((a,b))
            l,r = a,b
        #去掉完全相同的；
        dict = Counter(preEdges)
        edges =[ key for key in dict.keys() if dict[key]==1]

        #有可能全是相等的，直接空了
        if not edges:
            return 0
        #2.排序，把左边往前放，且把最长的边放前面，因为后面，可以看见的是大于这个边的，就是抻出去的的才能看见
        edges.sort(key=lambda x: (x[0],-x[1]))

        #3.开始遍历
        #因为从左到右排序的，下一个的左边界不会小于上一个，所以仅当下一个的右边界大于上一个的右边界，才能看见，否则就会被包在前一个里面
       
        res = 1
        rightEdge = edges[0][1]
        for a,b in edges:
            if b>rightEdge:
                res+=1
                rightEdge=b
        return res



'''
2345. Finding the Number of Visible Mountains
Medium
You are given a 0-indexed 2D integer array peaks where peaks[i] = [xi, yi] states that mountain i has a peak at coordinates (xi, yi). A mountain can be described as a right-angled isosceles triangle, with its base along the x-axis and a right angle at its peak. More formally, the gradients of ascending and descending the mountain are 1 and -1 respectively.

A mountain is considered visible if its peak does not lie within another mountain (including the border of other mountains).

Return the number of visible mountains.

 

Example 1:


Input: peaks = [[2,2],[6,3],[5,4]]
Output: 2
Explanation: The diagram above shows the mountains.
- Mountain 0 is visible since its peak does not lie within another mountain or its sides.
- Mountain 1 is not visible since its peak lies within the side of mountain 2.
- Mountain 2 is visible since its peak does not lie within another mountain or its sides.
There are 2 mountains that are visible.
Example 2:


Input: peaks = [[1,3],[1,3]]
Output: 0
Explanation: The diagram above shows the mountains (they completely overlap).
Both mountains are not visible since their peaks lie within each other.
 

Constraints:

1 <= peaks.length <= 105
peaks[i].length == 2
1 <= xi, yi <= 105'''