class Solution:
    def findExtra(self,n,a,b):
        #add code here
        s1=sum(a)
        s2=sum(b)
        s=s1-s2
        i=0
        j=n-1
        while i<=j:
            mid=(i+j)//2
            if a[mid]==s:
                return mid
            elif a[mid]<s:
                i=mid+1
            else:
                j=mid-1

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(Solution().findExtra(n, a, b))

# } Driver Code Ends