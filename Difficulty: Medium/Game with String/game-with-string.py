class Solution:
    def minValue(self, s, k):
        #code here        
        from collections import Counter
        import heapq
        hp=[-x for x in Counter(s).values()]
        heapq.heapify(hp)
        for _ in range(k):
            heapq.heapreplace(hp,hp[0]+1)
        return sum([x*x for x in hp])