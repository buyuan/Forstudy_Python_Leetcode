class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        #尝试用两头指针，如果值不相同，小的那个和相邻的加上，如果都相同，则往内部移动
        res=0
        left,right =0,len(nums)-1
        while left<right:
            if nums[left]==nums[right]:
                left+=1
                right-=1
            elif nums[left] < nums[right]:
                nums[left+1]+=nums[left]
                left+=1
                res+=1
            else:
                nums[right-1]+=nums[right]
                right-=1
                res+=1
        return res


'''
2422. Merge Operations to Turn Array Into a Palindrome
Medium
You are given an array nums consisting of positive integers.

You can perform the following operation on the array any number of times:

Choose any two adjacent elements and replace them with their sum.
For example, if nums = [1,2,3,1], you can apply one operation to make it [1,5,1].
Return the minimum number of operations needed to turn the array into a palindrome.

 

Example 1:

Input: nums = [4,3,2,1,2,3,1]
Output: 2
Explanation: We can turn the array into a palindrome in 2 operations as follows:
- Apply the operation on the fourth and fifth element of the array, nums becomes equal to [4,3,2,3,3,1].
- Apply the operation on the fifth and sixth element of the array, nums becomes equal to [4,3,2,3,4].
The array [4,3,2,3,4] is a palindrome.
It can be shown that 2 is the minimum number of operations needed.
Example 2:

Input: nums = [1,2,3,4]
Output: 3
Explanation: We do the operation 3 times in any position, we obtain the array [10] at the end which is a palindrome.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 106
'''