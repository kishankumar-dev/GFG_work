class Solution:
    def maxDotProduct(self, arr, brr):
        # code here
        m = len(brr)
        dp = [0] * (m + 1)
        for i, a in enumerate(arr):
            for j in reversed(range(min(i + 1, m))):
                dp[j + 1] = max(dp[j + 1], dp[j] + a * brr[j])
        return dp[m]