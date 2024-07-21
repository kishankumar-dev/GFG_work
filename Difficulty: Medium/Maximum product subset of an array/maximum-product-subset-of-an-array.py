#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    def findMaxProduct(self, arr):
        # Write your code here
        length = len(arr)
        prod = 1
        max_int = -float('inf')
        mod = 1000000007
        zero=0
        negative= 0
        for i in range(length):
            if arr[i]==0:
                zero+=1
                continue
            if arr[i]<0:
                negative+=1
                max_int = max(max_int,arr[i])
            prod = (prod*arr[i])
            if prod>0:
                prod = prod%mod
            
        if zero==length:
            return 0
        elif negative==1 and zero+negative==length:
            return 0
        elif negative%2==1:
            prod = prod//max_int
        return prod%mod


#{ 
 # Driver Code Starts.
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        arr = list(map(int, data[index:index + n]))
        index += n
        solution = Solution()
        ans = solution.findMaxProduct(arr)
        results.append(ans)
    
    for result in results:
        print(result)
# } Driver Code Ends