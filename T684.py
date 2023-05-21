class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        '''
        Union find,思路，把联通的节点放在一个集合（一个树）中，没次遇到一个新的边，从已有的树遍历
        如果各自能够找到共同的父节点，说明已经在树当中，进而说明这个新的边形成了环
        这个树的构建思路是用一个数组，数组的index是节点，值是父节点，对于值为初始值的index，说明是单独的节点，
        换句话说就是父节点是自己
        '''
        #题目规模，节点最多1000个，所以初始化一个1001个节点的数组
        parent = [-1]*1001
        res = []
        for edge in edges:
            parent1,parent2 = self.find(parent,edge[0]),self.find(parent,edge[1])
            if parent1==parent2:
                res = edge
            else:
                #新node加入树。parent2是第一个node的根节点，parent2是第二个节点放跟节点，都用跟节点，来赋值
                parent[parent1] = parent2
        return res
    def find(self,parent,node):
        #一直找到node节点的跟节点
        while parent[node]!=-1:
            node = parent[node]
        return node

'''
        
684. Redundant Connection
Medium
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.



Example 1:


Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
Example 2:


Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]


Constraints:

n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ai < bi <= edges.length
ai != bi
There are no repeated edges.
The given graph is connected.
'''