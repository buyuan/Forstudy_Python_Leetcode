class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #DP, dp[i,j],表示，word1 的前i个字母变成word2的前j个字母需要的步骤
        '''
        1. word[i]==word[j]:
        那么dp[i,j] = dp[i-1,j-1] ,即,当第i个字符和第j个字符相等时,不用做任何处理,
        "ac"->"bc", dp[1][1]=dp[0][0],不用针对最后一个c处理
        2. i==0, 则dp[0][j]=j, 即,插入j次
        "" ->"xx",  dp[0][1] = 2 ， 
        3. j==0, 则dp[i][0]=i, 即,删除j次
        4. 对于前i个字符变成前j个字符,根据前一个字符的状态,只有下面三种操作对应的可能
        dp[i-1][j]. word1的前i-1个字符convert成了word2的前j个字符,那么对于word1的第i个字符,做删掉动作 所以dp[i,j]=dp[i-1][j]+1
        dp[i][j-1],word1的前i个字符convert成了word2的前j-1个字符,那么再插入一个字符,就可以变成组成前word2的前j个字符 dp[i,j]=dp[i][j-1]+1
        dp[i-1][j-1], 当word1前i-1个字符变换为word2前j-1个字符,且word[i]!=word[j],那么把word1的第i个字符,replace为word2的第j个字符
        综上
        dp[i,j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
        '''
        l1,l2 = len(word1),len(word2)
        #下面 word1（i）当行用，word2（j)当列用,dp[i][j],从1开始，0位置是为了d[i-1]这类情况占位置
        dp = [[0]*(l2+1) for _ in range(l1+1)]
        for j in range(l2+1):
            #上面情况2
            dp[0][j]=j

        for i in range(l1+1):
            #上面情况3
            dp[i][0]=i
        
        for i in range(1,l1+1):
            for j in range(1,l2+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
        return dp[-1][-1]


'''
72. Edit Distance
Medium

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
 

Constraints:

0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.'''