from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        #计算字符点个数，单数个的字母,1的只能用一次，其他如果有用最大的,其他单数-1，或者通通-1，最后补一个1回来，其他的双数全都可以用
        mp = Counter(s)
        oddSum=0
        evenSum=0
        taken = False
        for value in mp.values():
            if value%2==0:
                oddSum+=value
            elif value==1 and not taken:
                evenSum+=1
                taken = True
            else:
                evenSum+=value-1
        #如果evenSum不等于0是因为没有拿过单个的1，则应该补回来，否则就使用那个单个的1在中间
        if evenSum!=0 and not taken:
            evenSum+=1
        return oddSum+evenSum

'''
09. Longest Palindrome
Easy
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
 

Constraints:

1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.'''