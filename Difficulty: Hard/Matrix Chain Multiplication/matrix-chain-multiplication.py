class Solution:
    def matrixMultiplication(self, arr):
        # code here
        n = len(arr)
        dp = [[float('inf')]*n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if j - i + 1 < 3:
                    dp[i][j] = 0
                else:
                    for k in range(i+1, j):
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + arr[i]*arr[k]*arr[j])
        return dp[0][-1]
        


#{ 
 # Driver Code Starts
# Initial Template for Python 3

t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().matrixMultiplication(arr)  # find the missing number
    print(s)  # print the result
    print("~")

# } Driver Code Ends