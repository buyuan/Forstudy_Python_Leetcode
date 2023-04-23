class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # 维护一个递减单调栈,记录的是坐标，排序的是值，然后再扫描num1，找到对应坐标，在nums2找出值
        # 值和坐标的映射，用来遍历nums1时候，找到对应坐标
        dic = {}
        stk = []
        # 下一个更大值的坐标
        match = [-1] * (len(nums2))
        for i in range(len(nums2)):
            dic[nums2[i]] = i
            while stk and nums2[i] > nums2[stk[len(stk) - 1]]:
                # 坐标top对应的下一个大值，坐标就是i
                match[stk[len(stk) - 1]] = i
                stk.pop()
            stk.append(i)
        res = []
        for item in nums1:
            index = dic[item]
            matchIndex = match[index]
            if matchIndex == -1:
                res.append(-1)
            else:
                res.append(nums2[matchIndex])
        return res
''' 
496. Next Greater Element I
Easy
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.



Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
Example 2:

Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.


Constraints:

1 <= nums1.length <= nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 104
All integers in nums1 and nums2 are unique.
All the integers of nums1 also appear in nums2.
'''