from collections import defaultdict
import math


class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        #每个点，挨个计算和别的点点斜率，如果点p1,p2 以及 p1,p3斜率相同，说明在同一个直线上，
        #并且注意累加相同的点
        n = len(points)
        ans =0
        for i in range(n):
            #循环可以取n-1,以便包含只有一个点的情况
            samePoint=1
            maxPointofSameSlope=0
            #这个map是记录point i 相同斜率的点，也就是point i同一个直线的点
            slope = defaultdict(int)
            Px,Py = points[i]
            for j in range(i+1,n):
                x,y = points[j]
                if Px==x and Py==y:
                    samePoint+=1
                else:
                    slp = self.getSlopt(Px,Py,x,y)
                    slope[slp]+=1
                    maxPointofSameSlope = max(maxPointofSameSlope,slope[slp])
            ans = max(ans,maxPointofSameSlope+samePoint)
        return ans

     #斜率的表示方法， 用两个点除去最大公约数，这样，回避了斜率精度问题，也解决了水平线和垂直线的表示
    def getSlopt(self,x1,y1,x2,y2):
        dx = x2-x1
        dy = y2-y1
        if dx==0:
            #vertical line，
            return (x1,0)
        if dy==0:
            #horizental line
            return (0,y1)
        #greatest common divisor
        gcd = math.gcd(dx,dy)
        #以分子分母形式返回,且，为了防止，（1，-1），（-1，1）这样，实际斜率相同但是表达不同的情况，统一把正负号放在第一位
        X,Y = dx/gcd,dy/gcd
        flag = 1 if X//Y>0 else -1
        return (flag*abs(X),abs(Y))


        




'''
149. Max Points on a Line
Hard
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

 

Example 1:


Input: points = [[1,1],[2,2],[3,3]]
Output: 3
Example 2:


Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
 

Constraints:

1 <= points.length <= 300
points[i].length == 2
-104 <= xi, yi <= 104
All the points are unique.'''