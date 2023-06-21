class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        #分别计算1，2和3，4的和的出现次数，在第二个集合中找第一个集合的相反数，找到说明存在等于0的和
        n=len(nums1)
        # sum:times
        mp_1_2 , mp_3_4={},{}
        for i in range(n):
            for j in range(n):
                times1 = mp_1_2.get(nums1[i]+nums2[j],0)
                mp_1_2[nums1[i]+nums2[j]]=times1+1

                times2 = mp_3_4.get(nums3[i]+nums4[j],0)
                mp_3_4[nums3[i]+nums4[j]]=times2+1
        res=0
        for k,v in mp_1_2.items():
            res+=v*mp_3_4.get(-k,0)
        return res
        
    #brute force
    def fourSumCount_bf(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        res=0
        
        for num1 in nums1:
            for num2 in nums2:
                for num3 in nums3:
                    for num4 in nums4:
                        if num1+num2+num3+num4==0:
                            res+=1
                            
        return res


'''
454. 4Sum II
Medium
Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:

0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
 

Example 1:

Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
Output: 2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
Example 2:

Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
Output: 1
 

Constraints:

n == nums1.length
n == nums2.length
n == nums3.length
n == nums4.length
1 <= n <= 200
-228 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 228
'''