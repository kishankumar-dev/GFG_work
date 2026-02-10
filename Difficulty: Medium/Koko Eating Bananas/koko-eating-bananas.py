class Solution:
    def kokoEat(self, arr, k):
        # Code here
        def ok(n):
            return sum((e+n-1)//n for e in arr) <= k
            
        lo, hi = 1, max(arr)
        while lo < hi:
            mi = lo + (hi - lo) // 2 
            if ok(mi):
                hi = mi 
            else:
                lo = mi+1
        return lo