class Solution:
    def longestWord(self, words: list[str]) -> str:
        res=""
        maxLen=0
        st = set(words)
        q=[]
        for wd in words:
            if len(wd)==1:
                q.append(wd)
        while q:
            cur = q.pop(0)
            if len(cur)>maxLen:
                maxLen = len(cur)
                res = cur
            elif len(cur)==maxLen:
                res = min(res,cur)
            for i in range(ord('a'),ord('z')+1):
                cur +=chr(i)
                if st.__contains__(cur):
                    q.append(cur)
                cur = cur[:-1]
        return res


'''
720. Longest Word in Dictionary
Mediu
Given an array of strings words representing an English Dictionary, return the longest word in words that can be built one character at a time by other words in words.

If there is more than one possible answer, return the longest word with the smallest lexicographical order. If there is no answer, return the empty string.

Note that the word should be built from left to right with each additional character being added to the end of a previous word.



Example 1:

Input: words = ["w","wo","wor","worl","world"]
Output: "world"
Explanation: The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
Example 2:

Input: words = ["a","banana","app","appl","ap","apply","apple"]
Output: "apple"
Explanation: Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".


Constraints:

1 <= words.length <= 1000
1 <= words[i].length <= 30
words[i] consists of lowercase English letters.
'''