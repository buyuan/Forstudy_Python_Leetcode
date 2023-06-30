import copy


class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        #其实就是求交集
        #倒叙是因为，list，pop比pop(0)更快
        points.sort(key=lambda x:x[0], reverse=True)
        res=0
        def findInterSection(r1:list[int],r2:list[int]):
            if not r1 or not r2:
                return None
            # r1的左边界一定大于等于r2的右边界（sort过的节点
            if r1[1]>r2[1]:
                return r2
            elif r1[1]>=r2[0]:
                return [r2[0],r1[1]]
            else:
                #r1[1]<r2[0]
                return None
        curP = points.pop()
        last = None
        while points:
            nextP= points.pop()
            temp = findInterSection(curP,nextP)
            if temp:
                #有交集
                curP=[temp[0],temp[1]]
            else:
                #没交集
                last = copy.deepcopy(curP)
                curP=copy.deepcopy(nextP)
                res+=1
        #检查最后一个范围，如果没有交集，那么就是两个不重叠的集合，res+1
        temp = findInterSection(last,curP)
        if not temp:
            res+=1
        return res

'''
452. Minimum Number of Arrows to Burst Balloons
Medium
There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

 

Example 1:

Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].
Example 2:

Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4
Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.
Example 3:

Input: points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
- Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].
 

Constraints:

1 <= points.length <= 105
points[i].length == 2
-231 <= xstart < xend <= 231 - 1'''