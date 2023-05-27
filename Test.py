import copy
class Solution(object):
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        st = set()
        for i in candidates:
            if i<=target:
                st.add(i)
        lst = list(st)
        res = []
        temp= []
        self.getCom(res,temp,lst,target,0)
        return res

    def getCom(self,res,temp,lst target,startpoint):
        if target<0:return
        if target==0:
            res.add(copy.deepcopy(temp))
            return
        for i in range(startpoint,len(lst)):
            temp.append(lst[i])
            self.getCom(res,temp,lst,target-lst[i],i)
            temp.pop()
