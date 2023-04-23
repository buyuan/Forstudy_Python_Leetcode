import heapq
class Solution:
    # 用快速排序的思路，从大到小，但是只用着眼于包含第k的数的那部分
    def partition(self,nums:list[int], left:int, right:int):
        pivot = nums[left]
        l = left+1
        while(l<=right):
            if nums[l]<pivot and nums[right]>pivot:
                #找到左边小的，右边大大，准备交换
                nums[l],nums[right] = nums[right], nums[l]
            #如果左边是大的，右边是小的，保留
            if nums[l]>=pivot:
                l+=1
            if nums[right]<=pivot:
                right-=1
        #最后把这个空位，放pivot进去
        nums[left],nums[right] = nums[right],nums[left]
        return right

    def findKthLargest(self, nums: list[int], k: int) -> int:
        left = 0
        right = len(nums)-1
        while(True):
            index = self.partition(nums,left,right)
            if index == k-1:
                return nums[index]
            elif index >k-1:
                #答案在大的那边，从大到小排列， 先k-1，后index
                right = index-1

            else:
                #答案在小的那边
                left = index+1

    def findKthLargest_heap(self, nums: list[int], k: int) -> int:
        #一个heap的联系
        #第k个大数字，就是倒数第len-k+1个最小
        heapq.heapify(nums)
        count = len(nums)-k
        while count>0:
            heapq.heappop(nums)
            count-=1
        return heapq.heappop(nums)



'''
215. Kth Largest Element in an Array
Medium
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

You must solve it in O(n) time complexity.



Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4


Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
'''