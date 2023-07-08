class Solution:
    def numberOfWays(self, s: str) -> int:
        #这个是leetcode的一些大佬给的题解
        #目的是数出来有多少个 101，和010，因为选三个，就这两种情况，
        #也是dp累加

        '''
        n0:以0 开头的组合有多少个，因此，只要遇到0，以0开头的组合就+1
        n1:以1 开头的组合有多少个，因此，只要遇到1，以1开头的组合就+1
        n10:开头两个数字是10的情况有多少个
        n01:开头两个数字是01的情况有多少个
        '''
        res,n0,n1,n10,n01=0,0,0,0,0
        for c in s:
            if c=="0":
                n0+=1   #0开头的情况+1，因为此时是一个新的0开头的情况
                n10+=n1 #新增10开头的个数就是前面所有单个1的个数，因为前面所有的1，都可以选出来和当前的0拼成10
                res+=n01#前面所有的01，都可以和现在这个0组合，成为010，符合要求
            else:  
                n1+=1
                n01+=n0
                res+=n10
        return res


    #下面这个dp超时了
    def numberOfWays_old(self, s: str) -> int:
        #dp[i][j][k], i表示考察到了index i的点，j表示前i个建筑已经选了j个，k表示类型（0，1）
        #到index i，则如果不选，条件是dp[i-1][j][k] ，j，k不变，只有i移动了，就是和上一个选了点一样
        #如果要选，条件是， dp[i-1][j-1][1-k],则上一个的条件是，选的比现在少一个，类型是另外一种
        #则dp[i][j][k]=dp[i-1][j][k]+dp[i-1][j-1][1-k]
        n=len(s)
        dp = [[[0]*2 for i in range(4)] for j in range(n+1)]
        dp[0][0][0] = 1
        dp[0][0][1] = 1
        #前面补一位，方便后面遍历开始
        s='s'+s
        for i in range(1,n+1):
            for j in range(4):
                for k in range(2):
                    #不选
                    dp[i][j][k]=dp[i-1][j][k]
                    #选了
                    if j>=1 and int(s[i])!=1-k:
                        dp[i][j][k]+=dp[i-1][j-1][1-k]
        return dp[n][3][0]+dp[n][3][1]

    def numberOfWays_bruteForce(self, s: str) -> int:
        #三重循环
        res=0
        def nextTarget(x):
            if x=="0":return "1"
            else :return "0"

        for i in range(len(s)-2):
            target1 = nextTarget(s[i])
            for j in range(i+1,len(s)-1):
                if s[j]==target1:
                    target2 = nextTarget(s[j])
                    for k in range(j+1,len(s)):
                        if s[k]==target2:
                            res+=1
        return res
        
'''
2222. Number of Ways to Select Buildings
Medium
You are given a 0-indexed binary string s which represents the types of buildings along a street where:

s[i] = '0' denotes that the ith building is an office and
s[i] = '1' denotes that the ith building is a restaurant.
As a city official, you would like to select 3 buildings for random inspection. However, to ensure variety, no two consecutive buildings out of the selected buildings can be of the same type.

For example, given s = "001101", we cannot select the 1st, 3rd, and 5th buildings as that would form "011" which is not allowed due to having two consecutive buildings of the same type.
Return the number of valid ways to select 3 buildings.

 

Example 1:

Input: s = "001101"
Output: 6
Explanation: 
The following sets of indices selected are valid:
- [0,2,4] from "001101" forms "010"
- [0,3,4] from "001101" forms "010"
- [1,2,4] from "001101" forms "010"
- [1,3,4] from "001101" forms "010"
- [2,4,5] from "001101" forms "101"
- [3,4,5] from "001101" forms "101"
No other selection is valid. Thus, there are 6 total ways.
Example 2:

Input: s = "11100"
Output: 0
Explanation: It can be shown that there are no valid selections.
 

Constraints:

3 <= s.length <= 105
s[i] is either '0' or '1'.'''