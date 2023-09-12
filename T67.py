class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n,m = len(a),len(b)
        if n<m:
            #确认哪个更长，方便后面把b加到a上
            a,b = b,a
            n,m=m,n
        ans =""
        digt=0
        for i in range(-1,-m-1,-1):
            tp = int(a[i])+int(b[i])+digt
            if tp<2:
                ans=str(tp)+ans
                digt=0
            else:
                digt=1
                ans=str(tp-2)+ans

        for i in range(-m-1,-n-1,-1):
            tp = int(a[i])+digt
            if tp<2:
                ans=str(tp)+ans
                digt=0
            else:
                digt=1
                ans=str(tp-2)+ans
        if digt:ans='1'+ans
        return anss





'''
67. Add Binary
Easy
8.6K
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.'''