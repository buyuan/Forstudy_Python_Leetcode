class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        #sort by the start
        intervals = sorted(intervals, key=lambda x: x[0])
        #merge
        result = []
        cur = [intervals[0][0], intervals[0][1]]
        for i in range(1,len(intervals)):
            if cur[1] < intervals[i][0]:
                result.append(cur)
                cur = intervals[i]
            else:
                cur[1] = max(intervals[i][1], cur[1])

        #incase only one item in interval or the last one merge not add
        if (len(result)==0)or (cur[1] != result[len(result)-1][1]):
            result.append(cur)
        return result


'''
56. Merge Intervals
Medium
17.3K
613
company
Amazon
company
Bloomberg
company
Facebook
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.



Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.


Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104

'''