class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #滑动窗口，这个窗口的长度，减去次数最多的字母差值小于等于K，则满足条件，一直扩大窗口到等于k
        #都大于k，左边界往右，缩小框，找到了，就往右走，看能不能查值变小，查值变小，右边界往右
        #用来记录这个区间内，字母出现的个数
        count=[0]*26
        res=0
        #出现最多的字母的个数
        maxAlp = 0
        #左边界
        left=0
        for i in range(len(s)):
            #当来到一个新的字符时，最多的字符只要比较一下这个新的字符和原来的字符哪个大，取大的这个就行
            index = ord(s[i])-ord('A')
            maxAlp = max(maxAlp,count[index]+1)
            count[index]+=1
            #i-left+1是i到left之间的字符个数，减去这个区间最多的字符的个数，如果仍然大于k，说明这个框太大，所以左边界往右，缩小
            while i-left+1-maxAlp>k:
                count[ord(s[left])-ord('A')]-=1
                left+=1
            #跳出来的条件肯定是<=k，说明符合条件,之后就是右边界，i继续往右，看有没有更大的框的可能
            res = max(res,i-left+1)
        return res



'''
424. Longest Repeating Character Replacement
Medium
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achive this answer too.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length'''