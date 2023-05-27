class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        #left, right各自n个，每次选择加入一个左边或者右边，
        res =[]
        self.helper(n,n,"",res)
        return res
    def helper(self,left,right,curString,res):
        #left用完了，或者right用完了，或者right多用了（left剩的多了），说明这个结果是错的，不用再继续
        if left<0 or right<0 or left>right:return
        if left==0 and right==0:
            res.append(curString)
            return
        self.helper(left-1,right,curString+"(",res)
        self.helper(left,right-1,curString+")",res)

'''
22. Generate Parentheses
Medium
18K
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:
Input: n = 1
Output: ["()"]
Constraints:
1 <= n <= 8'''