import collections


class Solution:
    def checkContradictions(self, equations: list[list[str]], values: list[float]) -> bool:
        #基本过程是，建立一个被除数的graph，存的是，所有相关的除数和商pair集合
        #然后遍历这个graph，通过被除数和存的商，计算除数的值，存在一个map中，然后验证这个值在其他的结果集中是否正确
        #同时，这个除数本身是其他节点的被除数，dfs下去
        def check_eq(a,b):
            return abs(a-b)< 1e-5

        graph=collections.defaultdict(set)
        for (a,b),r in zip(equations,values):
            if a==b:
                #直接验证
                if not check_eq(r,1):
                    #相等的两个数相除，结果不为1，是错误结果
                    return True
            else:
                graph[a].add((b,r))
                graph[b].add((a,1/r))
        #存的是被除数，除数变量对应的具体数字的值
        res = {}
        def dfs(dividend):
            for dividor,ratio in graph[dividend]:
                if dividor in res:
                    #如果res已经有了这个除数的值，就进行验证
                    if not check_eq(res[dividend]/res[dividor],ratio):
                        return True
                else:
                    #还没有这个除数的值，计算出来
                    res[dividor] = res[dividend]/ratio
                    #找到一个了dividor的值，那么开始dfs dividor
                    if dfs(dividor):
                        return True
            #所有的都通过检测，没有不一致，
            return False
        #开始实际搞
        for nd in graph:
            #nd是graph的key，实际就是对应的被除数的参数
            
            if not nd in res:
                #需要让程序先跑起来，给第一个计算的变量赋一个值，之后都根据这个初值计算
                #注意，这不是在解方程，因为这些等式实际没有固定解，缺少常数，可以自行验证
                res[nd]=2
            if dfs(nd):
                return True
        return False


'''
2307. Check for Contradictions in Equations
Hard

You are given a 2D array of strings equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] means that Ai / Bi = values[i].

Determine if there exists a contradiction in the equations. Return true if there is a contradiction, or false otherwise.

Note:

When checking if two numbers are equal, check that their absolute difference is less than 10-5.
The testcases are generated such that there are no cases targeting precision, i.e. using double is enough to solve the problem.
 

Example 1:

Input: equations = [["a","b"],["b","c"],["a","c"]], values = [3,0.5,1.5]
Output: false
Explanation:
The given equations are: a / b = 3, b / c = 0.5, a / c = 1.5
There are no contradictions in the equations. One possible assignment to satisfy all equations is:
a = 3, b = 1 and c = 2.
Example 2:

Input: equations = [["le","et"],["le","code"],["code","et"]], values = [2,5,0.5]
Output: true
Explanation:
The given equations are: le / et = 2, le / code = 5, code / et = 0.5
Based on the first two equations, we get code / et = 0.4.
Since the third equation is code / et = 0.5, we get a contradiction.
 

Constraints:

1 <= equations.length <= 100
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
Ai, Bi consist of lowercase English letters.
equations.length == values.length
0.0 < values[i] <= 10.0
values[i] has a maximum of 2 decimal places.'''