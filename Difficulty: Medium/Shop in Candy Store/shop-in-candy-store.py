from heapq import nlargest, nsmallest
class Solution:
    def minMaxCandy(self, prices, k):
        # code here
        n = len(prices)
        if k == 0:
            s = sum(prices)
            return s, s
        l = (n + k) // (k + 1)
        return sum(nsmallest(l, prices)), sum(nlargest(l, prices))