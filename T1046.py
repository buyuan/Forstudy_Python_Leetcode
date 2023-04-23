import heapq
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        #用phthon heapp，最小堆实现，因为stones都是正数，所以，负数push，取出来取反就是最大值
        hp=[]
        for item in stones:
            heapq.heappush(hp,-1*item)
        while len(hp)>1:
            l1 = -heapq.heappop(hp)
            l2 = -heapq.heappop(hp)
            cur = l1-l2 if l1<l2 else l2-l1
            if cur!=0:heapq.heappush(hp,cur)
        return 0 if not hp else -hp[0]

'''
1046. Last Stone Weight
Easy
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.



Example 1:

Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation:
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
Example 2:

Input: stones = [1]
Output: 1


Constraints:

1 <= stones.length <= 30
1 <= stones[i] <= 1000
'''