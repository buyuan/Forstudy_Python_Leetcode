import math


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        #类似T325的思路， 先建立一个前n项和的数组，因为都是正数，所以这个数组是递增的，
        #当这个数组的某个值为右边界时，往左找一个满足 右-左》=target的index

        accSum = [0]*len(nums)
        accSum[0] = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == target:
                #如果有直接相等的，不需要累加，肯定是答案
                return 1
            accSum[i] = accSum[i-1]+nums[i]
        ans = 0
        for i in range(0, len(nums)):
            temp = accSum[i]-target
            if temp<0:
                #前i项累计大于target，才有可能在这段中存在一个subarry
                continue
            elif temp ==0:
                '''
                    只有一次，且必然是第一次赋值，后面累加会越来越大，才可能继续找更小的ans
                if ans > 0:
                    ans = min(ans, i + 1)
                else:
                    ans = i + 1
                '''
                ans = i + 1
            else:
                left = self.findLeft(temp, i, accSum)
                if ans > 0:
                    ans = min(ans, i - left)
                else:
                    ans = i - left
        return ans

    def findLeft(self, target:int, right:int, accSum:list[int]):
        #需要找的就是小于等于temp的value的坐标中，找一个最靠右的
        ans=-1
        left =0
        while(right>left):
            mid = int(left+(right-left)/2)
            if accSum[mid] > target:
                right=mid-1
            else:
                left=mid+1
        if accSum[left]>target:
            # incase it just past to target
            left-=1
        if left >=0:
            ans =left
        return ans



'''
209. Minimum Size Subarray Sum
Medium
Given an array of positive integers nums and a positive integer target, return the minimal length of a
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.



Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0


Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
'''