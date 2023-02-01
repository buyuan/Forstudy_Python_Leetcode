class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        #找到需要融合的部分，然后merge，左右不干扰的分开寸
        left,right = newInterval[0], newInterval[1]
        l, r = [] , []
        for i in intervals:
            if i[0]>right:
                r.append(i)
            elif i[1]<left:
                l.append(i)
            else:
                left = min(left, i[0])
                right = max(right, i[1])
        mid = [left, right]
        l.append(mid)
        return l+r



'''
57. Insert Interval
Medium
company
Google
company
Amazon
company
Apple
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.



Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].


'''