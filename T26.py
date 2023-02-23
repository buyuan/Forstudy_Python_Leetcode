class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        #这个思路效率高，双指针，一个是当前，一个是下一个不重复的index，目的是把不重复的依次换到前面来，
        cur ,nextDif= 0,0
        while(nextDif<len(nums)):
            if nums[cur] == nums[nextDif]:
                nextDif+=1
            else:
                #找到不重复了,把不重复的放在cur的下一个,然后继续找下一个不重复
                cur+=1
                nums[cur] = nums[nextDif]
        #cur最后的值就是目标数组的最后一个坐标
        return cur+1


    def removeDuplicates_old(self, nums: list[int]) -> int:
        #这个效率太低，思路是找到重复是数量，然后把后面的数字往前移动
        mvCount=0
        ans = len(nums)
        i=1
        while(i <ans):
            if nums[i]==nums[i-1]:
                mvCount+=1
            else:
                if mvCount>0:
                    self.mvLeft(mvCount,i,nums)
                    #坐标要回到移动前第一个重复数字
                    i -= mvCount
                    ans -= mvCount
                    mvCount=0
            i += 1

        if mvCount > 0:
            self.mvLeft(mvCount, i, nums)
            ans -= mvCount
        return ans

    def mvLeft(self,count:int,startPoint:int,nums: list[int]):
        for i in range(startPoint,len(nums)):
            nums[i-count] = nums[i]


'''
26. Remove Duplicates from Sorted Array
Easy
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

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

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).


Constraints:

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.
'''