import copy
class Solution:
    def __init__(self):
        self.key = {
            '2':["a","b","c"],
            '3':["d",'e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
    def letterCombinations(self, digits: str) -> list[str]:
        res=[]
        self.helper("",res,digits,0)
        return res
    
    def helper(self,cur,res,digits,startpoint):
        if len(cur) == len(digits):
            res.append(copy.deepcopy(cur))
            return
        for i in range(startpoint,len(digits)):
            for value in self.key[digits[i]]:
                cur+=value
                self.helper(cur,res,digits,i+1)
                cur=cur[:-1]
    def test(self):
        print(self.key[2])
        for i in self.key[2]:
            print(i)




'''
17. Letter Combinations of a Phone Number
Medium
15.1K
Microsoft
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].'''