#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def modifyAndRearrangeArr (self, arr) : 
        #Complete the function
        s=len(arr)
        for i in range(0,s-1):
            if arr[i]!=0 and arr[i+1]!=0 and arr[i]==arr[i+1]:
                arr[i]=2*arr[i]
                arr[i+1]=0
        arr1=[0]*s
        count=0
        for i in range(0,s):
            if arr[i]!=0:
                arr1[count]=arr[i]
                count=count+1
        return arr1

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.modifyAndRearrangeArr(arr)
        print(*ans)
        t -= 1


# } Driver Code Ends