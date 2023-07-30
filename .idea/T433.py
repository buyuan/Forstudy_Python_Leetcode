
from collections import deque


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        #每次变换一个字母，如果
        st = set(bank)
        visited = set()
        genes = ["A","G","C","T"]
        que = deque()
        que.append(startGene)
        res=0
        while que:
            n=len(que)
            #每次遍历玩一个q，res+=1，因为这些都是变幻了一次字母，再一层，再加一，那些是变幻了一个字母之后，再变换一次
            for i in range(n):
                cur = que.popleft()
                if cur==endGene:return res
                for j in range(len(cur)):
                    #不能发现不等的基因，才变换，因为可能相差超过一个基因，所以，都要变，用bank来剪枝
                    #if cur[j]==endGene[j]:continue
                    ori = cur
                    for g in genes:
                        cur = cur[:j]+g+cur[j+1:]
                        if cur in st and cur not in visited:
                            que.append(cur)
                            visited.add(cur)
                    cur=ori
            res+=1
        return -1



        
'''
433. Minimum Genetic Mutation
Medium
A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene to endGene. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.

 

Example 1:

Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1
Example 2:

Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2
 

Constraints:

0 <= bank.length <= 10
startGene.length == endGene.length == bank[i].length == 8
startGene, endGene, and bank[i] consist of only the characters ['A', 'C', 'G', 'T'].'''