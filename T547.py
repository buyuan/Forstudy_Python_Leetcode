from collections import deque
class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        #通过一个城市，找到相关的所有城市，这是一个省
        #BFS遍历，未访问过的城市就是一个新的省的开始
        cities,cty_to_cities = len(isConnected[0]),len(isConnected)
        visited = [False]*cities
        res = 0
        for i in range(cities):
            if visited[i]:continue
            res+=1
            que = deque()
            que.append(i)
            visited[i]=True
            while que:
                curCity = que.popleft()
                for j in range(cty_to_cities):
                    if j==curCity:continue
                    if visited[j]:continue
                    if isConnected[curCity][j]==1:
                        #这两个城市链接，才能用j城市继续找，才算访问过该城市
                        que.append(j)
                        visited[j] = True
        return res





'''
547. Number of Provinces
Medium
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.



Example 1:


Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Example 2:


Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3


Constraints:

1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] is 1 or 0.
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]
'''