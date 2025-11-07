class Solution: 
    def maxProfit(self, jobs):
        from bisect import bisect_right
        from operator import itemgetter
        n = len(jobs)
        jobs.sort(key=itemgetter(1))
        dp = [0] * n
        dp[0] = jobs[0][2]
        for i in range(1, n):
            start, end, profit = jobs[i]
            j = bisect_right(jobs, start, key=itemgetter(1))
            if j > 0:
                profit += dp[j - 1]
            dp[i] = max(dp[i - 1], profit)
        return dp[-1]