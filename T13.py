class Solution:
    def __init__(self):
        self.note = {
            #value and rank
            "I":(1,1),
            "V" :(5,2),
            "X":(10,3),
            "L":(50,4),
            "C":(100,5),
            "D":(500,6),
            "M":(1000,7)
        }

    def romanToInt(self, s: str) -> int:
        res=0
        n=len(s)
        flag=1
        v0,r0 = self.note[s[n-1]]
        res+=v0
        for i in range(n-2,-1,-1):
            v,r =  self.note[s[i]]
            if r<r0:flag=-1
            else:flag=1
            res+=v*flag
            r0=r
        return res

'''
13. Roman to Integer
Easy

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].'''