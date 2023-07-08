class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        #单调栈的解法，用单调栈，找到第一个破坏non desc规则的数字，然后看它应该放在哪个位置，那个位置就是顺序变乱的开始或者结束
        n = len(nums)
        start,end=n,-1
        ascLst,descLst = [],[]
        for i in range(n):
            #单调递增栈
            while ascLst and nums[i]<nums[ascLst[-1]]:
                #一旦发现第i个数比上一个数小，就开始找第i个数应该放的位置，即，栈里面一直弹出直到nums[i]>ascLst[xx]
                #实际就是把中间的最小数字往左一直放到排序应该在的位置,不能用等号，因为需要子序列尽量小
                start = min(start,ascLst.pop())
            ascLst.append(i)

            #单调递减栈，从右往左，是单调递增栈相反的处理
            while descLst and nums[n-i-1]>nums[descLst[-1]]:
                #从右往左符合规则的是一个递减序列（非递增），所以，遇到一个变大的数，就要找到这个数字原本应该放在那里
                #实际最终就是把中间部分最大数字，放在最右边排序应该在的位置（按照递增，此时不能用等号）
                end=max(end,descLst.pop())
            descLst.append(n-1-i)
        if start==n:
            #是一个递增序列
            return 0
        return end-start+1
    def findUnsortedSubarray_arrayCompare(self, nums: list[int]) -> int:
        #排序，对比原数组，第一个换的和最后一个换的位置中间就是
        sortedNum = sorted(nums)
        l,r = -1,-1
        for i in range(len(nums)):
            if l==-1 and sortedNum[i]!=nums[i]:
                l=i
            elif sortedNum[i]!=nums[i]:
                r=i
        return 0 if l==-1 else r-l+1

    #下面这个方法边界有问题， 弃用
    def findUnsortedSubarray_incorrect(self, nums: list[int]) -> int:
        #从两头找，左边第一个变小的，右边第一额变大的
        l,r=-1,-1
        n = len(nums)
        #l想尽量往右，所以只有遇到严格小的才能算
        for i in range(n-1):
            if l<0 and nums[i]>nums[i+1]:
                l=i
                break
        if l==-1:
            #发现是一个递增数列
            return 0
        #找到左边界之后，往右走，找到第一个大于或等于左边界的点,这个是从左边往右找，符合要求的范围（不小于左边）
        lIndex = l+1
        while lIndex<n:
            if nums[lIndex]>=nums[l]:
                break
            lIndex+=1

        if lIndex==n:
            #到头了
            return n-l
        #r是从右往左，找到第一个比当前大的点，如果这个点在lIndex的左边，那么lIndex就是右边界
        #也可以理解为，两头相同的部分是没动的，剩下的都动了
        for i in range(n-1,0,-1):
            if nums[i]<nums[i-1]:
                r=i+1
                break
        r = max(r,lIndex)
        
        return r-l

'''
581. Shortest Unsorted Continuous Subarray
Medium
Given an integer array nums, you need to find one continuous subarray such that if you only sort this subarray in non-decreasing order, then the whole array will be sorted in non-decreasing order.

Return the shortest such subarray and output its length.

 

Example 1:

Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Example 2:

Input: nums = [1,2,3,4]
Output: 0
Example 3:

Input: nums = [1]
Output: 0
 

Constraints:

1 <= nums.length <= 104
-105 <= nums[i] <= 105
 '''