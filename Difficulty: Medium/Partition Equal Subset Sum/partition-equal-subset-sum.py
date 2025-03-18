class Solution:
    def equalPartition(self, arr):
        # code here
        s = sum(arr)
        if s&1 != 0:
            return False
        s >>= 1
        n = len(arr)
        dp = [[False]*(n+1) for _ in range(s+1)]
        for i in range(n+1):
            dp[0][i] = True
            
        for k in range(1, s+1):
            for i in range(n):
                dp[k][i+1] = dp[k][i]
                if arr[i] <= k:
                    dp[k][i+1] = dp[k][i+1] or dp[k-arr[i]][i]
        return any(dp[s])

#{ 
 # Driver Code Starts
import sys

input = sys.stdin.readline

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))

        ob = Solution()
        if ob.equalPartition(arr):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends