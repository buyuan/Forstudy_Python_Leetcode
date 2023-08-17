from collections import defaultdict
class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:

        oriMp = defaultdict(int)
        for word in words:
            oriMp[word]+=1
        num = len(words)
        singLen = len(words[0])
        sumLen = num*singLen
        ans = []
        for i in range(len(s)-sumLen+1):
            substr = s[i:i+singLen]
            if substr in oriMp:
                #这个字符存在，尝试判断是否一个组合
                curMp = defaultdict(int)
                start = i+singLen
                curMp[substr]+=1
                #遍历num个单词
                isAns=True
                #start-singLen是一开始的i位置，i+sumLen-singLen是最后一个单词的开头位置+1
                while start-singLen<i+sumLen-singLen:
                    #当前要处理的字符串是否在map中
                    curStr = s[start:start+singLen]
                    if curStr not in oriMp:
                        #如果没这个值
                        isAns=False
                        break
                    else:
                        frq = oriMp[curStr]
                        if curMp[curStr]+1>frq:
                            #当前这个子串个这个单词数量超了
                            isAns=False
                            break
                        else:
                            curMp[curStr]+=1
                    start+=singLen
                if isAns: ans.append(i)
        return ans

                    


        

'''
30. Substring with Concatenation of All Words
Hard

You are given a string s and an array of strings words. All the strings of wordfs are of the same length.

A concatenated substring in s is a substring that contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated substring because it is not the concatenation of any permutation of words.
Return the starting indices of all the concatenated substrings in s. You can return the answer in any order.

 

Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Since words.length == 2 and words[i].length == 3, the concatenated substring has to be of length 6.
The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.
The output order does not matter. Returning [9,0] is fine too.
Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
Explanation: Since words.length == 4 and words[i].length == 4, the concatenated substring has to be of length 16.
There is no substring of length 16 is s that is equal to the concatenation of any permutation of words.
We return an empty array.
Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]
Explanation: Since words.length == 3 and words[i].length == 3, the concatenated substring has to be of length 9.
The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"] which is a permutation of words.
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"] which is a permutation of words.
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"] which is a permutation of words.
 

Constraints:

1 <= s.length <= 104
1 <= words.length <= 5000
1 <= words[i].length <= 30
s and words[i] consist of lowercase English letters.'''