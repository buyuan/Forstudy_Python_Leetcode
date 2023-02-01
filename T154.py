class Solution:
    def findMin(self, nums: list[int]) -> int:
        #因为有可能左右两边相等，所以考虑当左右两边相等时，直接忽略相等的这个值
        left,right = 0,len(nums)-1
        while nums[0]==nums[right] and right!=0:
            right-=1
        ans = nums[0]
        while(left<right):
            mid = left+int((right-left)/2)
            ans = min(ans,nums[mid])
            if nums[mid]>nums[right]:
                #说明在上坡，所以应该往右找， 而mid肯定不是最小，因为大于right
                left=mid+1
            else:
                right = mid

        ans = min(ans,nums[left])
        return ans

'''
154. Find Minimum in Rotated Sorted Array II
Hard
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,4,4,5,6,7] might become:
[4,5,6,7,0,1,4] if it was rotated 4 times.
[0,1,4,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.
You must decrease the overall operation steps as much as possible.
Example 1:
Input: nums = [1,3,5]
Output: 1
Example 2:
Input: nums = [2,2,2,0,1]
Output: 0
Constraints:
n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
nums is sorted and rotated between 1 and n times.
'''