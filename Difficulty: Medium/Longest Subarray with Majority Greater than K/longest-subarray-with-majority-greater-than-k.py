class Solution:
    def longestSubarray(self, arr, k):
        # Code Here
        from itertools import accumulate
        arr = [-1 if e <= k else 1 for e in arr]
        acc = accumulate(arr)
        m, running, ans = {}, 0, 0
        for i, e in enumerate(acc):
            if e > 0: # e is already > 0, 0..i is good
                ans = max(ans, i+1) 
            if e not in m:
                m[e] = i
            if e-1 in m:
                ans = max(ans, i-m[e-1])
        return ans