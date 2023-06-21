class Solution:
    def makePalindrome(self, s: str) -> bool:
        #从中间往两头验证
        n = len(s)
        left,right=-1,-1
        if n%2==0:
            left,right = n//2-1,n//2
        else:
            left,right = n//2-1,n//2+1
        tolerance=2
        while left>-1 and right<n:
            if s[left]!=s[right]:
                if tolerance>0:
                    tolerance-=1
                else:
                    return False
            left-=1
            right+=1
        return True
            
'''
2330. Valid Palindrome IV
Medium
You are given a 0-indexed string s consisting of only lowercase English letters. In one operation, you can change any character of s to any other character.

Return true if you can make s a palindrome after performing exactly one or two operations, or return false otherwise.

 

Example 1:

Input: s = "abcdba"
Output: true
Explanation: One way to make s a palindrome using 1 operation is:
- Change s[2] to 'd'. Now, s = "abddba".
One operation could be performed to make s a palindrome so return true.
Example 2:

Input: s = "aa"
Output: true
Explanation: One way to make s a palindrome using 2 operations is:
- Change s[0] to 'b'. Now, s = "ba".
- Change s[1] to 'b'. Now, s = "bb".
Two operations could be performed to make s a palindrome so return true.
Example 3:

Input: s = "abcdef"
Output: false
Explanation: It is not possible to make s a palindrome using one or two operations so return false.
 

Constraints:

1 <= s.length <= 105
s consists only of lowercase English letters.
'''