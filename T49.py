
import copy


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        #排序一个单词，然后把index存入对应的map的value中
        mp = {}
        res=[]
        for i in range(len(strs)):
            cur = "".join(sorted(strs[i]))
            if mp.get(cur,-1)==-1:
                index = len(res)
                mp[cur]=index
                res.append([strs[i]])
            else:
                res[mp[cur]].append(strs[i])
        return res

'''
49. Group Anagrams
Medium
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.'''