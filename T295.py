class MedianFinder:

    def __init__(self):
        self.lst=[]
        self.len=0
    def addNum(self, num: int) -> None:
        if not self.lst:
            self.lst.append(num)
            self.len += 1
            return
        l,r = 0,self.len-1
        while l<r:
            mid = l+(r-l)//2
            if self.lst[mid]<num:
                l=mid+1
            else:
                r = mid
        if self.lst[l]>num:
            self.lst.insert(l,num)
        else:
            self.lst.insert(l+1, num)
        self.len += 1


    def findMedian(self) -> float:
        if self.len%2==0:
            #even
            return (self.lst[self.len//2]+self.lst[self.len//2-1])/2
        else:
            return self.lst[self.len//2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
'''
295. Find Median from Data Stream
Hard
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.


Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0


Constraints:

-105 <= num <= 105
There will be at least one element in the data structure before calling findMedian.
At most 5 * 104 calls will be made to addNum and findMedian.

'''