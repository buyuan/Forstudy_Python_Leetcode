import heapq


class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        #sort
        intervals = sorted(intervals, key = lambda x: x[0])
        # start from left, if conflict, add one room,
        #每个heap中的一个对象是一个会议室的结束时间，如果重合，则增加一个会议室，最后heap的size就是会议室数量
        #p排序就是为了可以从小到大安排，不会重复回去
        hp = []
        heapq.heappush(hp, intervals[0][1])
        for i in range(1, len(intervals)):
            if intervals[i][0] >= hp[0]:
                #没有冲突,后面更新
                heapq.heappop(hp)
            heapq.heappush(hp, intervals[i][1])
        return len(hp)




'''
253. Meeting Rooms II
6.3K
135
company
Bloomberg
company
Amazon
company
Google
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.



Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1
'''