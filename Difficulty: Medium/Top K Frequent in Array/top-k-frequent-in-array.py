import heapq
from collections import Counter
class Solution:
    def topKFreq(self, arr, k):
        freq=Counter(arr)
        heap=[(-val,-key) for key, val in freq.items()]
        heapq.heapify(heap)
        res=[]
        for _ in range(k):
            val,key=heapq.heappop(heap)
            res.append(-key)
        return res