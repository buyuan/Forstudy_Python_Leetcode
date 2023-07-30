import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        #binary search
        #可能的 范围是1～max(piles),二分法，从中间去一个值计算，如果大于h，说明吃少了，从大的吃，如果小于，说明吃多了
        l,r = 1,max(piles)
        res=r
        while l<=r:
            cur = l+(r-l)//2
            hours=0
            for p in piles:
                hours+=math.ceil(p/cur)
            if hours<=h:
                #时间少，说明吃得多，可以往小了吃
                res=min(res,cur)
                r=cur-1
            else:
                l=cur+1
        return res
        
'''
875. Koko Eating Bananas
Medium
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
 

Constraints:

1 <= piles.length <= 104
piles.length <= h <= 109
1 <= piles[i] <= 109'''