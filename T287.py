
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        #因为是1到n的值，如果有重复，则重复的这个值，会造成，小于等于这个值的个数比这个值本身多。（大于等于这个值的个数也比这个值本身多
        #目的就是找到这样一个值，通过不断缩小范围，比如小于， 或者大于，则重复值就是这个
        #left,right的作用其实是调节mid的位置，最后最后缩到，左右相等，就夹出来mid的位置，就是答案
        #下面不是坐标，是值
        left , right = 1,len(nums)-1
        while(left<right):
            #mid是一半的数量的个数
            mid = left+ int((right-left)/2)
            count=0
            for num in nums:
                if num<=mid:
                    count+=1
            if count>mid:
                #重复的数字肯定在mid之前，或者是mid因为肯定多了一个小于等于mid的值
                right = mid
            else:
                #这里面没有小于，只有等于，因为不可能小于，只要这个数组的值是连续的。
                #说明mid之前（包含mid）的都是不重复的
                left = mid+1
        return right


'''
287. Find the Duplicate Number
Medium
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.
Example 1:
Input: nums = [1,3,4,2,2]
Output: 2
Example 2:
Input: nums = [3,1,3,4,2]
Output: 3
Constraints:
1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.
'''