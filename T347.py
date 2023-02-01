import heapq
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        #1。用map统计 数字和频次
        #2 放到二维数组排序，
        #3 取前k个
        mp = {}
        for i in nums:
            cur = mp.get(i , 0)
            mp[i] = cur+1
        lst = []
        for j in mp.keys():
            lst.append([j, mp.get(j)])
        ans = []
        for i in range(0,k):
            ans.append(lst[i][0])
        return ans
'''
347. Top K Frequent Elements
Medium
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.



Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.


Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''