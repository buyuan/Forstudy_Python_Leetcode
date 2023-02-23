class Solution:
    def majorityElement_old(self, nums: list[int]) -> list[int]:
        ans = set()
        dic = {}
        length = len(nums)
        for num in nums:
            temp = dic.get(num,0)
            temp+=1
            if temp>int(length/3):
                ans.add(num)
            dic[num] = temp
        return list(ans)
    #下面这个是空间O（1）的算法，根据leetcode官方解法
    def majorityElement(self, nums: list[int]) -> list[int]:
    #Boyer - Moore Voting Algorithm，大致意思就是，用n个变量表示可能的n的结果集，比如，n/2 以上的，必然最多只有一个，n/3以上的，最多两个
    #计数的时候，是这个candidate，+1，不是，-1，如果到零，下一个就换下一个，真正超过n/m的结果能坚持到最后
        candidate1,candidate2,count1,count2 = None,None,0,0
        for num in nums:
            if candidate1 and candidate1==num:
                count1+=1
            elif candidate2 and candidate2==num:
                count2+=1
            elif count1==0:
                candidate1=num
                count1+=1
            #别忘了，if else是走到一个满足条件的分支就回去了,不需要手动保证can1不为空时候才能为c2
            #elif count2==0 and candidate1!=num:
            elif count2 == 0:
                candidate2=num
                count2+=1
            else:
                count1-=1
                count2-=1
        #确保两个candidate是真的超过n/3，因为如果没有答案的话，可能正好只是最后一个加了一
        ans = []
        for num in [candidate1, candidate2]:
            if nums.count(num)>len(nums)//3:
                ans.append(num)
        return ans

'''
229. Majority Element II
Medium
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.



Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]


Constraints:

1 <= nums.length <= 5 * 104
-109 <= nums[i] <= 109
'''