class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        res = []
        self.helper(res,"",4,s)
        return res

    def helper(self,res,curRes,leftParts,s):
        if leftParts==0:
            if len(s)==0:res.append(curRes)
            return
        for i in range(1,4):
                #尝试，1个数字，2个数字，3个数字的组合  
                if len(s)>=i and self.valid(s[:i]):
                    #剩余的字符至少有i个且这选中的数字符合条件才能继续
                    if leftParts==1:
                        #如果是最后一个段，不需要添加‘.'符号，所以传入的字符串不同  
                        self.helper(res,curRes+s[:i],leftParts-1,s[i:])
                    else:
                        #不是最后一段，需要补上'.'
                        self.helper(res,curRes+s[:i]+'.',leftParts-1,s[i:])
            
    def valid(self,s):
        #为空，超过3位数，超过1位数且以0开头，都是false
        if len(s)==0 or len(s)>3 or (len(s)>1 and s[0]=='0') :return False
        res = 0
        for digit in s:
            res = res*10+int(digit)
        return res<=255 and res>=0



'''
93. Restore IP Addresses
Medium
4.7K
A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

 

Example 1:

Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
Example 2:

Input: s = "0000"
Output: ["0.0.0.0"]
Example 3:

Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
 

Constraints:

1 <= s.length <= 20
s consists of digits only.
'''