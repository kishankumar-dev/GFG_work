class Solution:
    def maxProfit(self, prices):
        # code here
        n = len(prices)
        minv = prices[0]
        left = [0]*n
        for i in range(1, n):
            minv = min(minv, prices[i])
            left[i] = max(left[i-1], prices[i] - minv)
        
        maxv = prices[-1]
        right = [0]*n
        
        for i in range(n-2, -1, -1):
            maxv = max(maxv, prices[i])
            right[i] = max(right[i+1], maxv - prices[i])
            
        return max(l+r for l, r in zip(left, right))

#{ 
 # Driver Code Starts
#Initial template for Python 3
import math


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.maxProfit(arr))
        t -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends