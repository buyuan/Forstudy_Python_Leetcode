import heapq
import sys
# 练习Python的heapq,维护一个大小为k的堆
class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.hp=nums
        heapq.heapify(self.hp)
        self.k =k
        while len(self.hp)>k:
            heapq.heappop(self.hp)
    def add(self, val: int) -> int:
        heapq.heappush(self.hp,val)
        if len(self.hp)>self.k:
            heapq.heappop(self.hp)
        cur = heapq.heappop(self.hp)
        heapq.heappush(self.hp, cur)
        return cur


class KthLargest_old:
    #用一个有序数组存值
    def __init__(self, k: int, nums: list[int]):
        self.lst = nums
        self.lst.sort(reverse = True)
        self.k=k
    def add(self, val: int) -> int:
        left, right = 0, len(self.lst) - 1
        while left < right:
            mid = left + (right - left) // 2
            if self.lst[mid] < val:
                right = mid
            else:
                left = mid + 1
        self.lst.insert(left, val)
        return self.lst[self.k - 1]






# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

'''
703. Kth Largest Element in a Stream
Easy
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.


Example 1:

Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8


Constraints:

1 <= k <= 104
0 <= nums.length <= 104
-104 <= nums[i] <= 104
-104 <= val <= 104
At most 104 calls will be made to add.
It is guaranteed that there will be at least k elements in the array when you search for the kth element.
'''