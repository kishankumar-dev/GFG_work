#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        # code here
        t=n
        s=0
        while(t!=0):
            dig = t%10
            s = s + dig**3
            t//=10
        if s==n:
            return "Yes"
        else:
            return "No"


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = input()
        n=int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))
# } Driver Code Ends