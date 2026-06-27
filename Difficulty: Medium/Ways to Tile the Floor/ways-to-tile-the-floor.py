class Solution:
	def countWays(self, n, m):
		# Code here
		from collections import deque
        MODULO = 10**9 + 7
        dp = deque([1] * m)
        for i in range(m, n + 1):
            dp.append((dp.popleft() + dp[-1]) % MODULO)
        return dp[-1]