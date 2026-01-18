from collections import Counter
class Solution:
    def nextFreqGreater(self, arr):
        # code here
        cnt=Counter(arr)
        ret=[-1]*len(arr)
        stk=[]
        for ix,ve in enumerate(arr):
            while stk and cnt[arr[stk[-1]]]<cnt[ve]:
                ret[stk.pop()]=ve
            stk.append(ix)
        return ret