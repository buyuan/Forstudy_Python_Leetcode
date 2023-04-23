import heapq
from sys import maxsize


class SummaryRanges:

    def __init__(self):
        self.hp = []

    def addNum(self, value: int) -> None:
        if not len(self.hp):
            self.hp.append(value)
            return
        if value in self.hp:
            return
        l,r = 0,len(self.hp)-1
        while l<r:
            mid = l+(r-l)//2
            if self.hp[mid]<value:
                l = mid+1
            else:
                r = mid
        if self.hp[l]>value:
            self.hp.insert(l,value)
        else:
            self.hp.insert(l+1, value)

    def getIntervals(self) -> list[list[int]]:
        ans = []
        cur = []
        #python for出来不能修改i的值，改成while
        #for i in range(len(self.hp)):
        i=0
        while i<len(self.hp):
            cur.append(self.hp[i])
            while i<len(self.hp)-1 and self.hp[i+1]-self.hp[i]==1:
                i+=1
            cur.append(self.hp[i])
            ans.append(cur)
            cur = []
            i+=1
        return ans



# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
'''
352. Data Stream as Disjoint Intervals
Hard
Given a data stream input of non-negative integers a1, a2, ..., an, summarize the numbers seen so far as a list of disjoint intervals.

Implement the SummaryRanges class:

SummaryRanges() Initializes the object with an empty stream.
void addNum(int value) Adds the integer value to the stream.
int[][] getIntervals() Returns a summary of the integers in the stream currently as a list of disjoint intervals [starti, endi]. The answer should be sorted by starti.


Example 1:

Input
["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
[[], [1], [], [3], [], [7], [], [2], [], [6], []]
Output
[null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7, 7]], null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]

Explanation
SummaryRanges summaryRanges = new SummaryRanges();
summaryRanges.addNum(1);      // arr = [1]
summaryRanges.getIntervals(); // return [[1, 1]]
summaryRanges.addNum(3);      // arr = [1, 3]
summaryRanges.getIntervals(); // return [[1, 1], [3, 3]]
summaryRanges.addNum(7);      // arr = [1, 3, 7]
summaryRanges.getIntervals(); // return [[1, 1], [3, 3], [7, 7]]
summaryRanges.addNum(2);      // arr = [1, 2, 3, 7]
summaryRanges.getIntervals(); // return [[1, 3], [7, 7]]
summaryRanges.addNum(6);      // arr = [1, 2, 3, 6, 7]
summaryRanges.getIntervals(); // return [[1, 3], [6, 7]]


Constraints:

0 <= value <= 104
At most 3 * 104 calls will be made to addNum and getIntervals.
At most 102 calls will be made to getIntervals.
'''