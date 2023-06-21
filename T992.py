from collections import defaultdict


class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        #找不大于k个不同数字的数组的个数，减去不大于k-1个不同数字的数组
        return self.helper(nums,k)-self.helper(nums,k-1)

    def helper(self,nums,k):
        res=0
        dig_count=defaultdict(int)
        left=0
        #一个移动框，框的大小时left到i，每次找到符合条件的框（不同的数字个数小于等于k），则计算这个框中符合条件的数组的个数
        for i in range(len(nums)):
            if  dig_count[nums[i]]==0:
                #第一次出现这个数字，所以k-1
                k-=1
            #这个数字出现个数+1
            dig_count[nums[i]]+=1
            while k<0:
                #超过了k，所以要去掉一个数字，方法是左边界往右移动，移动时候，left所在的数字出现次数-1
                dig_count[nums[left]]-=1
                #如果left所在的数字已经没有，则说明框中独立的数字少了一个，k+1
                if dig_count[nums[left]]==0:k+=1
                #处理完后left右移
                left+=1
            #框的长度就是符合条件的数组的个数，框的右边界是固定的i
            #例如，【1，2，3，4】，右边界固定时，数组个数为，4，【1，2，3，4，】，【2，3，4】，【3，4】，【4】
            res+=i-left+1
        return res

    #below over timelimit
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        st= set()
        res=0
        for i in range(len(nums)):
            j=i
            while j<len(nums):
                st.add(nums[j])
                if len(st)>k:
                    break
                if len(st)==k:
                    res+=1
                j+=1
            st=set()
        return res

    def subarraysWithKDistinct_recordEveryArr(self, nums: list[int], k: int) -> int:
        st= set()
        res=[]
        for i in range(len(nums)):
            j=i
            cur=[]
            while j<len(nums):
                st.add(nums[j])
                if len(st)>k:
                    break
                cur.append(nums[j])
                if len(st)==k:
                    res.append(copy.deepcopy(cur))
                j+=1
            st=set()
        return len(res)


'''
992. Subarrays with K Different Integers
Hard
Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
Example 2:

Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
 

Constraints:

1 <= nums.length <= 2 * 104
1 <= nums[i], k <= nums.length
'''