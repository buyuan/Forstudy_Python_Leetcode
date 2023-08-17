class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1,n2,n3 =len(s1),len(s2),len(s3)
        if n1+n2!=n3:return False
        #dp[i][j]==true，表示s3[0:i+j]是由s1[0:i],s2[0:j]组成
        #占个位置，防止出现类似dp[-1]没有值的问题
        s1+='#'
        s2+='#'
        s3+='#'
        #n1, i当行用，n2, j当列用
        dp = [[0]*(n2+1) for i in range(n1+1)]

        #下面for循环的边界条件，dp[0][j],dp[i][0]需要赋值
        
        #dp[0][j]表示，只从n2出字符，看能匹配到多少s3，dp[i][0]表示，只从n1出字符，看能匹配到多少s3
        #啥也没有，或者说都是“#”符合
        dp[0][0]=1
        for i in range(1,n1+1):
            if dp[i-1][0] and s1[i]==s3[i]:
                dp[i][0]=1
        for j in range(1,n2+1):
            if dp[0][j-1] and s2[j]==s3[j]:
                dp[0][j]=1

        for i in range(1,n1+1):
            for j in range(1,n2+1):
                #检测下一个字符要是否可以从s1出，
                if dp[i-1][j] and s1[i]==s3[i+j]:
                    dp[i][j]=1
                elif dp[i][j-1] and s2[j]==s3[i+j]:
                    dp[i][j]=1
                   
        return dp[-1][-1]
'''
97. Interleaving String
Medium
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are divided into n and m 
substrings
 respectively, such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

 

Example 1:


Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Explanation: One way to obtain s3 is:
Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
Since s3 can be obtained by interleaving s1 and s2, we return true.
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Explanation: Notice how it is impossible to interleave s2 with any other string to obtain s3.
Example 3:

Input: s1 = "", s2 = "", s3 = ""
Output: true
 

Constraints:

0 <= s1.length, s2.length <= 100
0 <= s3.length <= 200
s1, s2, and s3 consist of lowercase English letters.
 

Follow up: Could you solve it using only O(s2.length) additional memory space?'''