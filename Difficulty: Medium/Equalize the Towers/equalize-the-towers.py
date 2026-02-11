from functools import cache
class Solution:
    def minCost(self, heights, cost):
        
        l, r = min(heights), max(heights)
        
        @cache
        def f(H):
            return sum(abs(h - H) * c for h, c in zip(heights, cost))
        
        while l < r:
            m = l + (r - l)//2
            
            if f(m+1) < f(m): # graph shape ~ \/ , find minima
                l = m+1
            else:
                r = m
        
        return f(l)