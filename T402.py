class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        #就是从左到右，尽可能保存小的数字，删掉大的数字，让高位树不要有大数字
        #维护单调栈，尽可能删除比栈顶大的数字k次
        # 如果删除数字比num长，直接返回0就行
        if k >= len(num): return '0'
        stk=[]
        for dgt in num:
            while stk and int(dgt)<int(stk[len(stk)-1]) and k>0:
                stk.pop()
                k-=1
            stk.append(dgt)
        #删除开头的0，
        while stk and stk[0] == '0': stk.pop(0)
        #如果循环完出现非递减序列，且k还有，从尾巴开始删除数字，因为删别的，这些大的数字往左移动，就会更大
        while stk and k > 0:
            stk.pop()
            k -= 1
        #如果为空，则返回0
        return "".join(stk) if stk else "0"



'''
402. Remove K Digits
Medium
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.



Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.


Constraints:

1 <= k <= num.length <= 105
num consists of only digits.
num does not have any leading zeros except for the zero itself.
'''