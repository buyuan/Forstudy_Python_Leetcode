import sys


class Solution:
    #超时
    def shortestWordDistance_timelimit(self, wordsDict: list[str], word1: str, word2: str) -> int:
        mp = {}
        for index, val in enumerate(wordsDict):
            cur = mp.get(val,[])
            cur.append(index)
            mp[val] = cur
        list1 = mp[word1]
        list2 = mp[word2]
        ans = sys.maxsize
        for i in list1:
            for j in list2:
                if i == j:
                    continue
                ans = min(ans,abs(i-j))
        return ans

    def shortestWordDistance(self, wordsDict: list[str], word1: str, word2: str) -> int:
        index1, index2 = -1, -1
        ans = sys.maxsize
        for index in range(0, len(wordsDict)):
            temp = index1
            if wordsDict[index] == word1:
                index1 = index
            if wordsDict[index] == word2:
                index2 = index
            if index1 != -1 and index2 != -1:
                if word1 == word2 and temp != -1 and temp != index2:
                    ans = min(ans, abs(temp - index1))

                elif index1 != index2:
                    ans = min(ans, abs(index1 - index2))
        return ans

'''
245. Shortest Word Distance III
Medium
Given an array of strings wordsDict and two strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.

Note that word1 and word2 may be the same. It is guaranteed that they represent two individual words in the list.



Example 1:

Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
Output: 1
Example 2:

Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "makes"
Output: 3


Constraints:

1 <= wordsDict.length <= 105
1 <= wordsDict[i].length <= 10
wordsDict[i] consists of lowercase English letters.
word1 and word2 are in wordsDict.
'''