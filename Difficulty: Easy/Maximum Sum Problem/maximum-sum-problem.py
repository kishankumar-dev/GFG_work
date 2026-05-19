class Solution:
    dp=[]
    def maxSum(self, n):
        if not Solution.dp:
            for i in range(1000000+1):
                if i<12:
                    Solution.dp.append(i)
                else:
                    Solution.dp.append(Solution.dp[i//2]+Solution.dp[i//3]+Solution.dp[i//4])
        return Solution.dp[n]