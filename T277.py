# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        #遍历，找一个col全1， 这个列的行只有唯一1的j
        found=True
        target = -1
        for j in range(n):
            for i in range(n):
                if not self.knows(i,j):
                    #如果有人不认识j,则j不是名人
                    found=False
                    break
            if found:
                #只有一个名人
                target = j
                break
            found =True
        for i in range(n):
            if i==target:
                continue
            if self.knows(target,i):
                #如果名人认识其他人，不是名人
                return -1
        return target
    def knows(self, i, j):
        matrix = [[1,1,0],[0,1,0],[1,1,1]]
        return matrix[i][j]==1

#1 1 0
#0 1 0
#1 1 1
'''
277. Find the Celebrity
Medium
Suppose you are at a party with n people labeled from 0 to n - 1 and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know the celebrity, but the celebrity does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. You are only allowed to ask questions like: "Hi, A. Do you know B?" to get information about whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).
You are given a helper function bool knows(a, b) that tells you whether a knows b. Implement a function int findCelebrity(n). There will be exactly one celebrity if they are at the party.
Return the celebrity's label if there is a celebrity at the party. If there is no celebrity, return -1.
Example 1:
Input: graph = [[1,1,0],[0,1,0],[1,1,1]]
Output: 1
Explanation: There are three persons labeled with 0, 1 and 2. graph[i][j] = 1 means person i knows person j, otherwise graph[i][j] = 0 means person i does not know person j. The celebrity is the person labeled as 1 because both 0 and 2 know him but 1 does not know anybody.
Example 2:
Input: graph = [[1,0,1],[1,1,0],[0,1,1]]
Output: -1
Explanation: There is no celebrity.
Constraints:
n == graph.length == graph[i].length
2 <= n <= 100
graph[i][j] is 0 or 1.
graph[i][i] == 1
 1 1 0
 0 1 0
 1 1 1
'''