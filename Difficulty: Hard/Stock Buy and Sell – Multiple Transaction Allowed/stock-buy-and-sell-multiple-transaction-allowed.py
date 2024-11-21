from typing import List


class Solution:
    def maximumProfit(self, prices) -> int:
        # code here
        res = 0
        n = len(prices)
        for i in range(1,n):
            if arr[i] > arr[i-1]:
                res += (arr[i] - arr[i-1])
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        solution = Solution()
        res = solution.maximumProfit(arr)
        print(res)

# } Driver Code Ends