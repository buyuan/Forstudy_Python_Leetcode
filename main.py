# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from T227  import Solution as S

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
class Node:
    def __init__(self, val: int = 0, left= None, right= None, next = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
import heapq
if __name__ == '__main__':
    #totalFileNumber()




    








