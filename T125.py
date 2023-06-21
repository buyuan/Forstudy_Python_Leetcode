class Solution:
    def isPalindrome(self, s: str) -> bool:
        i,j = 0,len(s)-1
        while i<j:
            while i<len(s) and not ( s[i].isalpha() or  s[i].isdigit()):
                i+=1
            while j>=0 and not ( s[j].isalpha() or  s[j].isdigit()):
                j-=1
            if i>j:
                return True
            if not s[i].lower()==s[j].lower():
                return False
            i+=1
            j-=1
        return True
'''
125. Valid Palindrome
Easy
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.'''