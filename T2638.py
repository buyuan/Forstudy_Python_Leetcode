from collections import defaultdict
from sortedcontainers import SortedList

class Solution:
    def countTheNumOfKFreeSubsets(self, nums: list[int], k: int) -> int:
        #same as 2597
        '''
        2597
        #DP,首先，将nums中的数字分组，将数字按k取模，相同余数的放在一组，因为除以k不同余数的数字之间相差不能是k，如果两个数相差是k
        #说明他们取模k余数肯定想等
        #不同组之间，因为互不相干，所以取法是相乘

        #对于同一组，先排序，验证相邻两个数是否可能差值为k，不相邻的不用验证，因为只有相邻的数字可能差值为k，不相邻的，至少是余数+k的差距
        #对于排序后，相同的数字，记录个数就可以，那么后面取到这个数字的时候，乘以这个次数的全排列减1（这个1是全都不取的时候），三个数字可以取任何一个，
        #任何两个。。。全部，也可以不取
        '''

        #按照除以k的余数分组
        mp=defaultdict(SortedList)
        for num in nums:
            mp[num%k].add(num)

        #各个组分别计算可以的组合，相乘
        res=1
        n = len(nums)
        for arr in mp.values():
            #take，nonTake实际是DP的思路，take[1],nonTake[i]是指，到index i，取该值的话，一共有多少种取值方法
            #以及 到index i，不取该值的话，一共有多少种取值方法
            #这样的话，结果其实就是，截止到最后一个数字，取值有多少结果和不取值有多少结果的和
            #因为直接取最后一个值，所以，直接用变量累加，不用再数组记录到最后然后取最后一个值了。
            take,nonTake=1,1
            for i in range(1,len(arr)):
                lastTake,lastNonTake = take,nonTake
                if abs(arr[i]-arr[i-1])==k:
                    take = lastNonTake
                    nonTake = lastTake+lastNonTake
                else:
                    take,nonTake = lastTake+lastNonTake,lastTake+lastNonTake
            #跳出来的结果是，最后一个数字take，和最和一个数字不take，有多少种取值方法
            res*=take+nonTake
        return res #全为空的那种选择法不用去除， 包含一个从0到n-1都是nonTake的组合


'''
2638. Count the Number of K-Free Subsets
Medium
You are given an integer array nums, which contains distinct elements and an integer k.

A subset is called a k-Free subset if it contains no two elements with an absolute difference equal to k. Notice that the empty set is a k-Free subset.

Return the number of k-Free subsets of nums.

A subset of an array is a selection of elements (possibly none) of the array.

 

Example 1:

Input: nums = [5,4,6], k = 1
Output: 5
Explanation: There are 5 valid subsets: {}, {5}, {4}, {6} and {4, 6}.
Example 2:

Input: nums = [2,3,5,8], k = 5
Output: 12
Explanation: There are 12 valid subsets: {}, {2}, {3}, {5}, {8}, {2, 3}, {2, 3, 5}, {2, 5}, {2, 5, 8}, {2, 8}, {3, 5} and {5, 8}.
Example 3:

Input: nums = [10,5,9,11], k = 20
Output: 16
Explanation: All subsets are valid. Since the total count of subsets is 24 = 16, so the answer is 16. 
 

Constraints:

1 <= nums.length <= 50
1 <= nums[i] <= 1000
1 <= k <= 1000'''