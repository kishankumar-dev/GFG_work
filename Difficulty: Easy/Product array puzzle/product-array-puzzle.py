#User function Template for python3

class Solution:
    def productExceptSelf(self, arr):
        #code here
        n = len(arr)
        res, lp, rp = [1]*n, [1]*n, [1]*n
        lp[0], rp[n-1] = arr[0], arr[n-1]
        tmp = 1
        for i in range(1,n):
            lp[i] =  lp[i-1]*arr[i]
            rp[n-1-i] = rp[n-i]*arr[n -1 - i]
        res[0], res[n-1] = rp[1], lp[n-2] 
        for i in range(1,n-1):
            res[i] = (lp[i-1]*rp[i+1])
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):

        arr = [int(x) for x in input().split()]

        ans = Solution().productExceptSelf(arr)
        print(*ans)
        print("~")

# } Driver Code Ends