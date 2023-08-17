class Solution:

    #5*2才有0，所以要求有多少个5，有多少个5就有多少个0
    def trailingZeroes(self, n: int) -> int:
        if n==0: return 0
        return n//5+self.trailingZeroes(n//5)

    def trailingZeroes(self, n: int) -> int:
        res = 1
        while n>0:
            res*=n
            n-=1
        ans=0
        while res>10 and res%10==0:
            ans+=1
            res//=10

        return ans


'''
172. Factorial Trailing Zeroes
Medium
Given an integer n, return the number of trailing zeroes in n!.

Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

 

Example 1:

Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Example 3:

Input: n = 0
Output: 0
 

Constraints:

0 <= n <= 104'''