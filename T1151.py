class Solution:
    def minSwaps(self, data: list[int]) -> int:
        #确定一个框的大小，容纳所有的1，然后用这个大小的框从头移动到尾，找到过程中最多的1，
        #最多1的框和所有的1的差值，就是需要把其他1移动过来的个数
        size = 0
        for i in data:
            #因为值是1，所以合就是个数
            if i==1:
                size+=1
        left = 0
        curOne=0
        maxOne=0
        for i in range(len(data)):
            if i-left+1>size:
                if data[left]==1:
                    curOne-=1
                left+=1
            if data[i]==1:
                curOne+=1
                maxOne = max(maxOne,curOne)
        return size-maxOne

'''
1151. Minimum Swaps to Group All 1's Together
Medium
Given a binary array data, return the minimum number of swaps required to group all 1’s present in the array together in any place in the array.

 

Example 1:

Input: data = [1,0,1,0,1]
Output: 1
Explanation: There are 3 ways to group all 1's together:
[1,1,1,0,0] using 1 swap.
[0,1,1,1,0] using 2 swaps.
[0,0,1,1,1] using 1 swap.
The minimum is 1.
Example 2:

Input: data = [0,0,0,1,0]
Output: 0
Explanation: Since there is only one 1 in the array, no swaps are needed.
Example 3:

Input: data = [1,0,1,0,1,0,0,1,1,0,1]
Output: 3
Explanation: One possible solution that uses 3 swaps is [0,0,0,0,0,1,1,1,1,1,1].
 

Constraints:

1 <= data.length <= 105
data[i] is either 0 or 1.'''