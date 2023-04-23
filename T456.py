import sys


class Solution:

    def find132pattern(self, nums: list[int]) -> bool:
        #用单调递减栈,整体思路就是，我让第二，第三个数字都尽量大，一旦找到比第三个数字小的，就找到了答案
        #先设定132的第三个数，栈里面放所有大于这个第三数的值，作为132中的3，且是递减的放
        #目的是保证金第二个数一直大于第三个数，且尽量让第二第三个数大，这样找到更小的第一个数更有可能性
        #从后往前遍历，因为是从132中的2先构建，然后是3，
        #在遍历过程中， 如果遇到的数字，比栈的最后一个数字大，那么就将栈中的，比当前遍历数字小且左边大于当前遍历数字的数字，赋值给
        #第三个数，然后将当前遍历到的数字入栈，这样即让第三个数字变大，右能找到更大的备选数字（132中的3）
        #当遇到比第三个数小的数字时候，就找到了答案，因为stk中的数字比第三数大
        third = -(sys.maxsize-1)
        stk=[]
        for i in range(len(nums)-1,-1,-1):
            cur = nums[i]
            if cur<third:return True
            while stk and cur>stk[len(stk)-1]:
                #如果目前这个数，比栈的最后一个数字大，要做的就是将它放在刚好比它大的那个数字后面，且把这个数字后面那个刚好比他小
                #的数字赋值给third，然后再把当前数字加入到栈
                #这样，第二个，第三个数字都更大了，
                third = stk.pop()
            stk.append(cur)
        return False



'''
456. 132 Pattern
Medium
Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.



Example 1:

Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.
Example 2:

Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
Example 3:

Input: nums = [-1,3,2,0]
Output: true
Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
'''