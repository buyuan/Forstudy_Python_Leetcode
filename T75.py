class Solution:
    #思路是，先找到各个颜色的起始位置，然后遍历，每次走到一个点，要做的事情就是判断，如果这个点不是正确的颜色，就把它和正确颜色
    #的位置的点交换，一直递归，直到这个点颜色正确为止，正确位置有数据之后，注意坐标的后移
    def findTheRightPlace(self,nums:list[int],iR:int,iW:int,iB:int,index:int) -> None:
        if index < iW:
            # should be red
            if nums[index] == 0:
                return
            else:
                if nums[index] == 1:
                    nums[index], nums[iW] = nums[iW], nums[index]
                    iW+=1
                    self.findTheRightPlace(nums,iR,iW,iB,index)
                else:
                    # ==2
                    nums[index], nums[iB] = nums[iB], nums[index]
                    iB += 1
                    self.findTheRightPlace(nums, iR, iW, iB, index)
        elif index >= iW and index < iB:
            # ==1
            if nums[index] == 1:
                return
            else:
                if nums[index] == 0:
                    nums[index], nums[iR] = nums[iR], nums[index]
                    iR+=1
                    self.findTheRightPlace(nums,iR,iW,iB,index)
                else:
                    # ==2
                    nums[index], nums[iB] = nums[iB], nums[index]
                    iB += 1
                    self.findTheRightPlace(nums, iR, iW, iB, index)
        else:
            # ==2
            if nums[index] == 2:
                return
            else:
                if nums[index] == 1:
                    nums[index], nums[iW] = nums[iW], nums[index]
                    iW+=1
                    self.findTheRightPlace(nums,iR,iW,iB,index)
                else:
                    # ==0
                    nums[index], nums[iR] = nums[iR], nums[index]
                    iR += 1
                    self.findTheRightPlace(nums, iR, iW, iB, index)

    def sortColors_1(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 先找到三种颜色的数量，确定各自开始的坐标，然后从0开始扫描，找到以后和各自坐标交换
        cR,cW,cB = 0,0,0
        for i in range(0, len(nums)):
            if nums[i]==0:
                cR+=1
            elif nums[i]==1:
                cW+=1
            else:
                cB+=1
        iR = 0
        iW = cR
        iB = cR+cW
        for i in range(0, len(nums)):
            self.findTheRightPlace(nums, iR, iW, iB, i)


     #还有一种思路，把0放到最开头（和左边指针交换），把2放到最后（和右边指针交换），剩下的1就在中间
    def sortColors_2(self, nums: list[int]) -> None:
        iR = 0
        iB = len(nums) - 1
        i=0
        # iB以后的就是不需要再扫的，因为已经归位
        #突然发现 for i in range(), 第一次赋值就定了，不能再改，即便range里面是变化的
        while(i<iB+1):
            if nums[i] == 0:
                # red
                nums[i], nums[iR] = nums[iR], nums[i]
                iR += 1
            elif nums[i] == 2 :
                # blue
                nums[i], nums[iB] = nums[iB], nums[i]
                iB -= 1
                #以防交换过来的是0，再检测一次
                i-=1
            else:
                # white
                pass
            i +=1


'''
75. Sort Colors
Medium
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.



Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]


Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.

'''