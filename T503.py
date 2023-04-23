class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        stk=[]
        n=len(nums)
        res=[-1]*n
        #往前再走一次，就相当于多循环了一圈，所以是2n
        for i in range(2*n):
            num = nums[i%n]
            #这个的思路是，我依次把元素放进去（放下标是为了方便知道位置），栈内的元素实际就是一个不递增的序列
            #因为当发现下一个数字大的时候，就找到了答案，然后把当前栈顶去掉，然后栈顶就是前一个数字，继续比较
            while stk and nums[stk[len(stk)-1]]<num:
                res[stk[len(stk)-1]] = num
                stk.pop()
            if i<n:
                stk.append(i)
        return res

'''
503. Next Greater Element II
Medium
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.



Example 1:

Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2;
The number 2 can't find next greater number.
The second 1's next greater number needs to search circularly, which is also 2.
Example 2:

Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]


Constraints:

1 <= nums.length <= 104
-109 <= nums[i] <= 109
'''