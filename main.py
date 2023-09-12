# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import heapq
import timeit

from T909 import Solution as s
import os
path = "./"
def totalFileNumber(pth=path):
    files = os.listdir(pth)
    count=0
    for file in files:
        if file in ["main.py","Test.py"]: continue
        if not file.startswith("T"):continue
        if file.endswith('.py'):
            count+=1
    print(count)

if __name__ == '__main__':
    totalFileNumber()



        

    '''
    # a sample of timeit
    lst1 = [3 for i in range(100000)]
    lst2 = [3 for i in range(100000)]
    def que(lst):
        n=len(lst)
        while n>0:
            lst.pop(0)
            n-=1
    def stk(lst):
        n=len(lst)
        while n>0:
            lst.pop()
            n-=1

    res = timeit.timeit(
        stmt="que(lst1)",
        setup = "from __main__ import que,lst1",
        number = 1000)

    print(f'this is the result of que:  {res}')
    res = timeit.timeit(
        stmt="stk(lst2)",
        setup="from __main__ import stk,lst2",
        number=1000)

    print(f'this is the result of stk: {res}')
    '''





    








