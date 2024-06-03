#User function Template for python3
class Solution:
    def numberOfConsecutiveOnes (ob,n):
        # code here 
        mod = int(1e9+7)
        a, b, c = 0, 1, 0
        for i in range(2, n+1):
            # power of two can blow up fast so, keep running mod
            a, b, c = b, (a+b)%mod, ((c*2) % mod + b)%mod
        return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        N = int(input())

        ob = Solution()
        print(ob.numberOfConsecutiveOnes(N))

# } Driver Code Ends