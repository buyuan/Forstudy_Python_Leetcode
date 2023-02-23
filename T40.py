class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        #类似39，只是同一个位置的值不能重复,因为是要unique的组合， 要考虑去掉重复
        #方法，排序数组，然后循环到和前一个相同的数字时，跳过，因为如果是需要连续相同的数字，第一个就能找全，如果不需要，
        #即只要这一个数字的时候，跳后后面相同的就可以
        candidates.sort()
        temp=[]
        ans=[]
        self.findCombine(candidates,temp,ans,0,target)
        return ans

    def findCombine(self, lst:list[int], temp:list[int], ans:list[list[int]], startPoint:int, target:int):
        if target<0:return
        if target==0:
            ans.append(temp.copy())
            return
        for i in range(startPoint,len(lst)):
            if i>startPoint and lst[i]==lst[i-1]:
                continue
            temp.append(lst[i])
            self.findCombine(lst, temp, ans, i+1, target-lst[i])
            temp.pop()



'''
40. Combination Sum II
Medium
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.



Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output:
[
[1,2,2],
[5]
]


Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
'''