class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        #尝试先去重，然后再用二分法
        st = set()
        newList = []
        for i in range(0,len(nums)):
            if st.__contains__(nums[i]):
                continue
            newList.append(nums[i])
            st.add(nums[i])

        #开始二分法，参考33,注意，left是上半区的左，right是下半区的右
        left=0
        right = len(newList)-1

        while(left+1<right):
            mid = left+int((right-left)/2)
            if newList[mid]==target:
                return True
            if newList[mid]>=newList[right]:
                #上半区,此时，left也在上半区，用确定的上半区数据来比较
                if newList[mid]>=target and target>=newList[left]:
                    right = mid
                else:
                    left=mid
            else:
                #下半区，用确定的下半区数据比较（right）
                if target<=newList[right] and target>=newList[mid]:
                    left=mid
                else:
                    right=mid

        if newList[left]==target:
            return True
        if newList[right]==target:
            return True
        return False

'''
81. Search in Rotated Sorted Array II
Medium
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.



Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false


Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
nums is guaranteed to be rotated at some pivot.
-104 <= target <= 104

'''