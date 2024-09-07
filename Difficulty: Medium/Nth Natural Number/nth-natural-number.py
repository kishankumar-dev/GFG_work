#User function Template for python3

class Solution:
    def findNth(self,n):
        #code here
        ret=0
        pl=0
        while n>0:
            ret+=n%9*10**pl
            pl+=1
            n//=9
        return ret

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for i in range(0, t):
    n = int(input())
    obj = Solution()
    s = obj.findNth(n)
    print(s)

# } Driver Code Ends