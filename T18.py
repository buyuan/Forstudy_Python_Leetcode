class Solution(object):
    def quick(self, nums, left, right):
        if left<right:
            l = left
            r = right
            pivot = nums[left]
            while l<r:
                #从右往左，找一个比pivot小的
                while l<r and nums[r]>pivot:
                    r-=1
                #跳出来，说明发现找到小的了
                if l<r:
                    #把大的这个数放在原来pivot的位置
                    nums[l]= nums[r]
                    l+=1
                #从左到右，找一个比pivot大的
                while l<r and nums[l]<pivot:
                    l+=1
                if l<r:
                    #把大的放在上面换过来的哪个小的数的位置
                    nums[r]=nums[l]
                    r-=1
            #出来以后就是left，right相遇，此时，把pivot放在这个位置，那么，左边都比pivot小，右边都大
            nums[r] = pivot
            self.quick(nums,left,r-1)
            self.quick(nums, r+1, right)




    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        #1 order， 练一练快排，思想是，找到一个基准，然后从两边找，把小于基准的放在左边，大于的放在右边，然后以基准最终落到的位置
        #拆分两段，各自再继续相同处理
        self.quick(nums,0,len(nums)-1)
        #2 check, 2sum加一层是3sum，3sum加一层是4sum,注意排除重复
        ans = []
        for i in range(len(nums)-3):
            if i>0 and nums[i] == nums[i-1]: continue
            for j in range(i+1, len(nums)-2):
                #3sum
                if j >i+1 and nums[j]==nums[j-1]:continue
                left,right = j+1,len(nums)-1
                while left<right:
                    #2sum
                    sum = nums[i]+nums[j]+nums[left]+nums[right]
                    if sum ==target:
                        ans.append([nums[i],nums[j],nums[left],nums[right]])
                        while left<right and nums[left]==nums[left+1]:
                            left+=1
                        while left<right and nums[right]==nums[right-1]:
                            right-=1
                        #因为不能重复，所以，nums[left],nums[right]任何一个保留都会导致答案只能是另一个
                        left+=1
                        right-=1
                    elif sum<target:
                        #需要大的
                        left+=1
                    else:
                        right-=1
        return ans







'''
18. 4Sum
Medium

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.



Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]


Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
'''