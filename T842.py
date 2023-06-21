import copy
import sys


class Solution:
    def splitIntoFibonacci(self, num: str) -> list[int]:
        cur = []
        self.res = []

        def helper(cur,num,startPoint):
            #RES 中有一个答案，就可以返回了
            if self.res:return
            #有三个以上的数据段，且用完了num，说明这个答案符合条件
            if len(cur)>=3 and startPoint>=len(num):
                self.res=copy.deepcopy(cur)
                return
            
            #然后从start point、开始，一次1个数字，一次2个数字，一直到最后
            for i in range(startPoint,len(num)):
                curNum = num[startPoint:i+1]
                #0开头或者长度大于10位（超过题目限制）这个数字就无效，再往后都没有意义  
                '''
                if (len(curNum)>1 and curNum[0]=='0') or len(curNum)>10:break
                cNum = int(curNum)
                if cNum>sys.maxsize: break
                '''
                if len(curNum)>1 and curNum[0]=='0' :break
                cNum = int(curNum)
                if cNum>2**31 - 1: break
                #检查是否符合fibonacacci数列
                if len(cur)>=2 and (cur[-1]+cur[-2]!=cNum) :continue
                cur.append(cNum)
                helper(cur,num,i+1)
                #还原
                cur.pop()

        helper(cur,num,0)
        return self.res




'''
842. Split Array into Fibonacci Sequence
Medium
1K
287
company
Amazon
You are given a string of digits num, such as "123456579". We can split it into a Fibonacci-like sequence [123, 456, 579].

Formally, a Fibonacci-like sequence is a list f of non-negative integers such that:

0 <= f[i] < 231, (that is, each integer fits in a 32-bit signed integer type),
f.length >= 3, and
f[i] + f[i + 1] == f[i + 2] for all 0 <= i < f.length - 2.
Note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number 0 itself.

Return any Fibonacci-like sequence split from num, or return [] if it cannot be done.

 

Example 1:

Input: num = "1101111"
Output: [11,0,11,11]
Explanation: The output [110, 1, 111] would also be accepted.
Example 2:

Input: num = "112358130"
Output: []
Explanation: The task is impossible.
Example 3:

Input: num = "0123"
Output: []
Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.'''