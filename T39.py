class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        #先用一个set，做一些剪枝
        st = set()
        for num in candidates:
            if num<=target:
                st.add(num)
        lst = list(st)
        ans =[]
        temp=[]
        self.findCombine(ans,temp,lst,0,target)
        return ans

    def findCombine(self,ans:list[list[int]], temp:list[int], lst:list[int], startPoint:int, target:int):
        if target<0: return
        if target==0:
            #这里会有前拷贝的问题，被append进去ans的对象是temp指向的对象，会根据temp变化而变化，所以用一个copy
            ans.append(temp.copy())
            return
        for i in range(startPoint, len(lst)):
            #从当前开始往后找，如果每次都从0开始找，会有很多重复，，
            temp.append(lst[i])
            self.findCombine(ans,temp,lst,i,target-lst[i])
            temp.pop()





'''
39. Combination Sum
Medium
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
frequency
 of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.



Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []


Constraints:

1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40
'''