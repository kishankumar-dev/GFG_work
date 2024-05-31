#User function Template for python3
class Solution:
    def swapNibbles (self, n):
        # code here
        g=format(n,"08b")
        s=g[4:]+g[0:4]
        
        t=int(s,2)
        return t


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        print(ob.swapNibbles(n))

# } Driver Code Ends