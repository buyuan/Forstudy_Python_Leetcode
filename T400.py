import math


class Solution:
    def findNthDigit(self, n: int) -> int:
        #先找到这个数字属于哪个段， 几位数段数字段
        if n<10:
            return n
        digits =1
        base = 9
        start =1
        while True:
            if n <=base*digits:
                break
            n -= base * digits
            digits+=1
            base*=10
            start*=10
        #向上取整，是因为只要超过，就进入下一个数字，start已经是第一个了，所以减1个,
        start +=math.ceil(n/digits)-1
        sStart = str(start)
        seq =0
        if n%digits==0:
            seq = digits
        else:
            seq= n%digits
        return int(sStart[seq-1])





'''
400. Nth Digit
Medium
Given an integer n, return the nth digit of the infinite integer sequence [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...].



Example 1:

Input: n = 3
Output: 3
Example 2:

Input: n = 11
Output: 0
Explanation: The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.


Constraints:

1 <= n <= 231 - 1
'''