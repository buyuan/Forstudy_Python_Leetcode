class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        #把前面不重复的1个或者两个往前放
        #先检查，确实有一个还是两个，然后再换
        length = len(nums)
        curIndex,flag=0,False
        for nextDif in range(1,length):
            if nums[nextDif-1]==nums[nextDif]:
                nextDif+=1
                flag=True
            else:
                nums[curIndex]=nums[nextDif-1]
                curIndex+=1
                if flag:
                    nums[curIndex] = nums[nextDif - 1]
                    curIndex += 1
                flag = False
        #最后一个数字可能来不及修改就跳出了循环，curIndex-1是最后一个被修改的位置
        if nums[curIndex-1]!=nums[length-1]:
            nums[curIndex] = nums[length-1]
            curIndex += 1
            if flag:
                nums[curIndex] = nums[length - 1]
                curIndex+=1
        if curIndex==0:
            #说明没有做值的交换，肯定是数组值一样，或者为空
            #如果超过2个数字，则保留两个，所以index到1，返回下一个(2), 如果只有一个数字，index是0，返回1，1就是长度
            return min(length,2)
        return curIndex

'''
80. Remove Duplicates from Sorted Array II
Medium
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.



Example 1:

Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).


Constraints:

1 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
'''