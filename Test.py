from collections import deque


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k>=len(num):return '0'
        #monotonic inscresing stack, remove k times when new number is smaller
        #means remove the left big number
        stk=deque()
        for dgt in num:
            while stk and int(dgt)<int(stk[-1]) and k>0:
                stk.pop()
                k-=1
            stk.append(dgt)
        #删除开头的0
        while stk and stk[0]=='0':
            stk.popleft()
        #if more k left, delete from right, cannot delete from left, or a larger num will be move to left
        while stk and k>0:
            stk.pop()
            k-=1
        return "".join(stk) if stk else "0"


