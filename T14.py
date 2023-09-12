class trie:
    def __init__(self,val=''):
        self.subNode={}
        #self.isWord=False
        self.val=val
        self.prefix=""
        self.end=False


class Solution:
    def longestCommonPrefix_Python(self, strs: list[str]) -> str:
        ans=[]
        for l in (x for x in zip(*strs)):
            temp =set()
            for y in l:
                temp.add(y)
            if len(temp)>1:
                break
            ans.append(temp.pop())
        return "".join(ans)

    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs)==1:return strs[0]
        for s in strs:
            if not s:return ""
        #练习一下用字典树
        root = trie()
        for word in strs:
            self.buildTrie(root,word)
        if len(root.subNode)>1:return ""
        else:root=root.subNode[strs[0][0]]
        while root:
            if  len(root.subNode)>1 or root.end :return root.prefix
            for k in root.subNode.keys():
                root=root.subNode[k]

    def buildTrie(self,root,word):
        cur = root
        for chr in word:
            curPrefix = cur.prefix
            if not cur.subNode.__contains__(chr):     
                cur.subNode[chr]=trie(chr)
            cur=cur.subNode[chr]
            cur.prefix = curPrefix+chr
        cur.end=True
            

        

'''
14. Longest Common Prefix
Easy
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.'''