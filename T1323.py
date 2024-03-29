class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num)
        res = int(s[0])
        if res==6:
            return int('9'+s[1:])
        flag = True
        for i in range(1,len(s)):
            if  flag and s[i]=='6':
                flag=False
                res=res*10+9
                continue
            res=res*10+int(s[i])
        return res

    def maximum69Number_2(self, num: int) -> int:
        s = str(num)
        for i in range(len(s)):
            if s[i] == '6':
                if i == len(s) - 1:
                    return int(s[:i] + "9")
                else:
                    return int(s[:i] + "9" + s[i + 1:])
        return num



'''
1323. Maximum 69 Number
Easy
You are given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).



Example 1:

Input: num = 9669
Output: 9969
Explanation:
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666.
The maximum number is 9969.
Example 2:

Input: num = 9996
Output: 9999
Explanation: Changing the last digit 6 to 9 results in the maximum number.
Example 3:

Input: num = 9999
Output: 9999
Explanation: It is better not to apply any change.


Constraints:

1 <= num <= 104
num consists of only 6 and 9 digits.
'''