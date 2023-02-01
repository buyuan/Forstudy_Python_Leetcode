import sys
class Solution:
    def shortestDistance(self, wordsDict: list[str], word1: str, word2: str) -> int:
        mp = {}
        for index in range(0,len(wordsDict)):
            cur = mp.get(wordsDict[index],[])
            cur.append(index)
            mp[wordsDict[index]] = cur
        iList1 = mp.get(word1)
        iList2 = mp.get(word2)
        ans = sys.maxsize
        for i in iList1:
            for j in iList2:
                ans = min(ans,abs(i-j))
        return ans
'''
243. Shortest Word Distance
Easy
Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.
Example 1:
Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
Output: 3
Example 2:
Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
Output: 1
Constraints:
2 <= wordsDict.length <= 3 * 104
1 <= wordsDict[i].length <= 10
wordsDict[i] consists of lowercase English letters.
word1 and word2 are in wordsDict.
word1 != word2
'''