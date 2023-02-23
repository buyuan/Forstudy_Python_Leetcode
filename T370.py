class Solution:

    #下面这个超时，估计要先合并updates，然后在处理数组
    def getModifiedArray_old(self, length: int, updates: list[list[int]]) -> list[int]:
        ans = [0]*length
        for update in updates:
            for i in range(update[0], update[1] + 1):
                ans[i] += update[2]
        return ans


    def getModifiedArray(self, length: int, updates: list[list[int]]) -> list[int]:
        #换一种理解，把start到end之间的数据加上val，相当于把start到结尾，都+val，然后从end+1到结尾再-val
        #意思就是，从start开始，后面都加val，从end+1开始后面都加-val，这个思路预处理updates，建立一个累加数组
        accumulateArray = [0]*(length+1)
        for update in updates:
            accumulateArray[update[0]] +=update[2]
            accumulateArray[update[1]+1]-=update[2]
        sum = 0
        ans = []
        for i in range(length):
            sum+=accumulateArray[i]
            ans.append(sum)
        return ans



'''
370. Range Addition
Medium
You are given an integer length and an array updates where updates[i] = [startIdxi, endIdxi, inci].

You have an array arr of length length with all zeros, and you have some operation to apply on arr. In the ith operation, you should increment all the elements arr[startIdxi], arr[startIdxi + 1], ..., arr[endIdxi] by inci.

Return arr after applying all the updates.
Example 1
Input: length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
Output: [-2,0,3,5,3]
Example 2:

Input: length = 10, updates = [[2,4,6],[5,6,8],[1,9,-4]]
Output: [0,-4,2,2,2,4,4,-4,-4,-4]
Constraints:

1 <= length <= 105
0 <= updates.length <= 104
0 <= startIdxi <= endIdxi < length
-1000 <= inci <= 1000
'''