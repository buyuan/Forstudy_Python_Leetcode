class Solution:
    def countPrimes(self, n: int) -> int:
        # 埃拉托斯特尼筛法 Sieve of Eratosthenes
        #从2开始，扫描到n-1，标记每个质数的倍数，是倍数则不是质数，扫描完，没被标记的就是质数
        #从1到n-1，0好位置忽略
        isPrime = [True]*n
        res = 0
        for i in range(2,n):
            #已标记的非质数，跳过
            if not isPrime[i]:continue
            res+=1
            multi=2
            while i*multi<n:
                isPrime[i*multi]=False
                multi+=1
        return res

'''
204. Count Primes
Medium
Given an integer n, return the number of prime numbers that are strictly less than n.



Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0


Constraints:

0 <= n <= 5 * 106
'''