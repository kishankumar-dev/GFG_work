class Solution:
    def sumSubstrings(self,s):
        # code here
        n = len(s)
        dp = [0]*(n+1)
        for i in range(1, n+1):
            d = ord(s[i-1]) - ord('0')
            dp[i] = dp[i-1]*10 +d*i
        return sum(dp)