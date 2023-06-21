class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        #找到最大值，最小值的坐标，计算交换最大值之后，最小值的坐标会有什么变化
        #然后计算最大值坐标和终点差值，以及最小值坐标和起点差值，以及最大值交换对最小值的影响
        larIndex,smlIndex=0,0
        max,min=nums[0],nums[0]
        for i in range(len(nums)):
            if nums[i]>=max:
                #找等号，是因为希望max是最右边的，
                max = nums[i]
                larIndex=i
            elif nums[i]<min:
                #不用等号，是因为希望min更靠左
                min = nums[i]
                smlIndex=i
        if smlIndex==larIndex:
            #就一个数字：
            return 0
        if smlIndex<larIndex:
            return (smlIndex-0)+(len(nums)-1-larIndex)
        if smlIndex>larIndex:
            #有交叉，larIndex 交换后，smlIndex会往左走一步
            return (smlIndex-1-0)+(len(nums)-1-larIndex)



    #下面这个方法不行，因为不需要的交换十几也做了交换，只是次数清零，但是却改变了数组原来的顺序
    def minimumSwaps_false(self, nums: list[int]) -> int:
        #两次循环，第一次，从左到右，如果左大右小就交换，交换后，如果这个被交换的比右边小，清空前面的交换次数，就是说，换了半天不是最大的
        #第二次从右到左，类似于第一次，只不过换大的改成换小的
        resL = 0
        index =0
        n = len(nums)
        while index <n-1:
            if resL and nums[index]<=nums[index+1]:
                resL=0 
            elif nums[index]>nums[index+1]:
                nums[index+1], nums[index] = nums[index], nums[index+1]
                resL+=1
            index+=1
        resS = 0
        while index>0:
            if resS and nums[index]>=nums[index-1]:
                resS=0
            elif nums[index]<nums[index-1]:
                nums[index], nums[index-1] = nums[index-1],nums[index]
                resS+=1
            index-=1
        return resL+resS
'''
You are given a 0-indexed integer array nums.

Swaps of adjacent elements are able to be performed on nums.

A valid array meets the following conditions:

The largest element (any of the largest elements if there are multiple) is at the rightmost position in the array.
The smallest element (any of the smallest elements if there are multiple) is at the leftmost position in the array.
Return the minimum swaps required to make nums a valid array.

 

Example 1:

Input: nums = [3,4,5,5,3,1]
Output: 6
Explanation: Perform the following swaps:
- Swap 1: Swap the 3rd and 4th elements, nums is then [3,4,5,3,5,1].
- Swap 2: Swap the 4th and 5th elements, nums is then [3,4,5,3,1,5].
- Swap 3: Swap the 3rd and 4th elements, nums is then [3,4,5,1,3,5].
- Swap 4: Swap the 2nd and 3rd elements, nums is then [3,4,1,5,3,5].
- Swap 5: Swap the 1st and 2nd elements, nums is then [3,1,4,5,3,5].
- Swap 6: Swap the 0th and 1st elements, nums is then [1,3,4,5,3,5].
It can be shown that 6 swaps is the minimum swaps required to make a valid array.
Example 2:
Input: nums = [9]
Output: 0
Explanation: The array is already valid, so we return 0.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105
'''