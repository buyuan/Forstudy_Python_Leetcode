from collections import defaultdict
from sortedcontainers import SortedList

class Solution:
    def beautifulSubsets(self, nums: list[int], k: int) -> int: 
        #DP,首先，将nums中的数字分组，将数字按k取模，相同余数的放在一组，因为除以k不同余数的数字之间相差不能是k，如果两个数相差是k
        #说明他们取模k余数肯定想等
        #不同组之间，因为互不相干，所以取法是相乘

        #对于同一组，先排序，验证相邻两个数是否可能差值为k，不相邻的不用验证，因为只有相邻的数字可能差值为k，不相邻的，至少是余数+k的差距
        #对于排序后，相同的数字，记录个数就可以，那么后面取到这个数字的时候，乘以这个次数的全排列减1（这个1是全都不取的时候），三个数字可以取任何一个，
        #任何两个。。。全部，也可以不取

        #1。预处理数据，将不同余数的数字去重分组，并且记录重复数据的次数
        dic=defaultdict(SortedList) # key: 余数，value：相同余数的数字的集合，用sorted_set，可以在加入后排序
        freq=defaultdict(int) #用来记录超过一次的重复数据
        for num in nums:
            md = num%k
            freq[num]+=1
            if freq[num]>1:continue #去除重复数字
            dic[md].add(num)

        #2 DP 分组计算后相乘
        res=1
        def calComb(lst,k,freq):
            #take[i]表示如果在第i个index，拿这个数字，有多少种组合
            #nonTake[i]表示在第i个index，不拿这个数字，有多少种组合
            n = len(lst)
            if n==1:
                #只有一个数字，进不了循环，直接计算
                fre=freq[lst[0]]
                return 2**fre #这里是全排列，因为去掉空集统一在最外部的return处理
            take,nonTake=[0]*n,[0]*n
            nonTake[0]=1
            #根据lst第一个数字的频次，计算take[1]的值
            take[0] = 2**freq[lst[0]]-1
            for i in range(1,n):
                fre=freq[lst[i]]
                if abs(lst[i]-lst[i-1])==k:
                    #如果当前数字那，则上一个数字不拿的集合数字，乘以当前数字的不同取值组合，如果只有一个那么就是种类
                    take[i] = nonTake[i-1]*(2**fre-1)
                    #如果当前数字不拿，那么上一个位置，拿不拿都符合要求
                    nonTake[i] = take[i-1]+nonTake[i-1]
                else:
                    take[i] = (take[i-1]+nonTake[i-1])*(2**fre-1)
                    nonTake[i] = take[i-1]+nonTake[i-1]
            #最后一个拿不拿都可以
            return take[n-1]+nonTake[n-1]
            
        for lst in dic.values():
            res*=calComb(lst,k,freq)
        #去除空集
        return res-1

    def beautifulSubsets_dfs(self, nums: list[int], k: int) -> int: #超时了
        #dfs
        def dfs(curIndex,taken,nums,k):
            if curIndex>=len(nums):
                #遍历完了没有不符合条件的，是一个解
                return 1
                
            #visited可以用数组，表示哪些坐标已经取过，这里用二进制数表，1表示取过，0表示没取
            takenFlag = 1
            for i in range(curIndex):
                #根据curIndex之前的元素确定， curIndex取不取
                if ((taken>>i) & 1) and abs(nums[curIndex]-nums[i])==k:
                    #如果taken的第i个位置是1，且两个元素差值=k，则不取
                    takenFlag=0
                    break #目前这个序列往下走没意义了
            take = dfs(curIndex+1,taken+(1<<curIndex),nums,k) #cur下一个位置，taken加上一个1左移cur位
            nontake = dfs(curIndex+1,taken,nums,k)
            if takenFlag:
                return take+nontake
            else:
                return nontake


        return dfs(0,0,nums,k)-1 #去掉空集
        
'''
2597. The Number of Beautiful Subsets
Medium
You are given an array nums of positive integers and a positive integer k.

A subset of nums is beautiful if it does not contain two integers with an absolute difference equal to k.

Return the number of non-empty beautiful subsets of the array nums.

A subset of nums is an array that can be obtained by deleting some (possibly none) elements from nums. Two subsets are different if and only if the chosen indices to delete are different.

 

Example 1:

Input: nums = [2,4,6], k = 2
Output: 4
Explanation: The beautiful subsets of the array nums are: [2], [4], [6], [2, 6].
It can be proved that there are only 4 beautiful subsets in the array [2,4,6].
Example 2:

Input: nums = [1], k = 1
Output: 1
Explanation: The beautiful subset of the array nums is [1].
It can be proved that there is only 1 beautiful subset in the array [1].
 

Constraints:

1 <= nums.length <= 20
1 <= nums[i], k <= 1000'''