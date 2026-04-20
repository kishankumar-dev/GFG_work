from functools import cache
class Solution:
    def derangeCount(self, n: int) -> int:
        # code here
        @cache
        def count(mask, i):
            if i > n:
                return 1
            cnt = 0
            for j in range(1, n+1):
                if mask&(1<<j) == 0 and j != i:
                    cnt += count(mask|(1<<j), i+1)
            return cnt
        return count(0, 1)