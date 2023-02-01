
class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        # sort
        intervals = sorted(intervals, key = lambda x: x[0])

        #check
        for i in range(1, len(intervals)):
            if intervals[i-1][1]>intervals[i][0]:
                return False

        return True




'''

252. Meeting Rooms
1.7K
86
company
Google
company
Bloomberg
company
Amazon
Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.



Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: true
'''