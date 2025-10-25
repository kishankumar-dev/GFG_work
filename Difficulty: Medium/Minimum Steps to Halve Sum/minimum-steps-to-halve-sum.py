import heapq
class Solution:
    def minOperations(self, arr):
    # code here
        n = len(arr)
        heap = []
        target = sum(arr) / 2
        for i in arr:
            heapq.heappush(heap, -i)
        s, cnt = sum(arr), 0
        while(heap):
            if s <= target:
                return cnt
            cnt += 1
            ele = (-heapq.heappop(heap)) / 2
            s = s - ele
            heapq.heappush(heap, -ele)
        return cnt

