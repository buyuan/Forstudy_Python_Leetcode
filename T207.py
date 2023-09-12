
from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        #这个方法是建立一个入度数组，数组的下标是课程，值是课程需要的先修课程
        #然后从入度为0的开始扫描，给对应的后续课程的入度减1，然后把新的入度为0的课加入，
        #扫描完之后，如果所有课程入度都为0，说明可以修完
        indegree = [0]*numCourses
        #简历前置课程和后续课程的map，方便后续寻找
        mp=defaultdict(set)        
        for course in prerequisites:
            after ,pre =course
            indegree[after]+=1
            mp[pre].add(after)
        q = []
        for i in range(numCourses):
            if indegree[i]==0:q.append(i)

        while q:
            cur = q.pop()
            for index in mp[cur]:
                indegree[index]-=1
                if indegree[index]==0:
                    q.append(index)
        return sum(indegree)==0
        

    #下面是一个可行的方法，有向图是否有环来验证
    def canFinish_2(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        #1 先建立一个课程和前序课程的图，其实是一个有向图
        graph=defaultdict(set)
        for course in prerequisites:
            k ,v =course
            graph[k].add(v)
        visited = [0]*numCourses
        #2.遍历课程图，如果课程所在的图有环，则无法完成，判断有向图是否有环，可以用DFS，一条路走到头，如果没有重复，则无环
        visited =set()
        visiting =set()
        for i in range(numCourses):
            if self.dfs(i,visited,visiting,graph):return False
        return True

    def dfs(self,node,visited,visiting,graph):
        if node in visiting:return True #found circle
        if node in visited: return False #
        visiting.add(node)
        for n in graph[node]:
            if self.dfs(n,visited,visiting,graph):
                return True
        visiting.remove(node)
        visited.add(node)
        return False



    #因为一个课程可能有多个前序，所以这个是个图，不是链表，下面的用链表的方法不行，但是思路是一样的
    def canFinish_old(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        #相当于一个或多个链表，遍历，如果发现环，不可能完成，如果遍历完，所有课程都遍历过，则tru
        #1，建立课程和前序的map,前序课程可能是多个
        mp=defaultdict(set)
        for course in prerequisites:
            k ,v =course
            mp[k].add(v)
        visited = [0]*numCourses
        #2 开始遍历课程
        for i in range(numCourses):
            if visited[i]:continue
            visited[i]=1
            if i in mp:
                #如果这个是链表中的一个节点，开始遍历链表，链表中不能有环
                st=set()
                q = deque()
                q.append(i)
                while q:
                    #因为q是这一次课程的所有前序，所以需要遍历完确定是否有套
                    n=len(q)
                    for j in range(n):
                        curCourse=q.popleft()
                        #链表有环，说明课程前序变成连环套了
                        if curCourse in st:return False
                        st.add(curCourse)
                        visited[curCourse]=1
                        #有可能这个课程的前序也是多个
                        for c in mp[curCourse]:
                            q.append(c)
                            visited[curCourse]=1
        return True







        
'''
207. Course Schedule
Medium

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.'''