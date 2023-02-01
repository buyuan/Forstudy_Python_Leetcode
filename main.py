# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from T154  import Solution as S

import bisect

def displayB(board:list[list[int]]):
    for lst in board:
        for lter in lst:
            print(lter,end=" ")
        print("\n")
if __name__ == '__main__':
    s = S()
    nums =[1,3,5]
    target = 3
    board=[["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
    word = "ABCESEEEFS"
    print(s.findMin(nums))


