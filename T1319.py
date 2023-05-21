from collections import deque, defaultdict


class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        #n个电脑需要n-1 个网线链接，所以先判断网线够不够
        if len(connections)<n-1:return -1
        #有n个不连接的电脑组，就需要移动n-1个网线把他们互相练起来
        #visited = [0]*n
        visited=set()
        que = deque()
        clusters = 0
        #创建一个数据结构，表示某个电脑和所有他可以到达的电脑的关系
        #con是一个数组， con[0]存0号电脑相连的电脑,
        '''
        # 下面这个声明有问题，因为初始化了一个set，数组中引用的全是同一个set
        con = [set()] * n
        '''
        con =[ set() for i in range(n)]
        for a,b  in connections:
            con[a].add(b)
            con[b].add(a)



        for i in range(n):
            if i in visited: continue
            clusters += 1
            #visited[i] = 1
            visited.add(i)
            que.append(i)
            while que:
                cur = que.popleft()
                for item in con[cur]:
                    if item not in visited:
                        que.append(item)
                        visited.add(item)
        return clusters - 1





'''
1319. Number of Operations to Make Network Connected
Medium
There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where connections[i] = [ai, bi] represents a connection between computers ai and bi. Any computer can reach any other computer directly or indirectly through the network.

You are given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.

Return the minimum number of times you need to do this in order to make all the computers connected. If it is not possible, return -1.
Example 1:


Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.
Example 2:


Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
Output: 2
Example 3:

Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
Output: -1
Explanation: There are not enough cables.


Constraints:

1 <= n <= 105
1 <= connections.length <= min(n * (n - 1) / 2, 105)
connections[i].length == 2
0 <= ai, bi < n
ai != bi
There are no repeated connections.
No two computers are connected by more than one cable.
'''