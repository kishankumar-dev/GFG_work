#User function Template for python3

def max_sum(a,n):
    maxi, res, totalSum = 0, 0, 0
    
    for i in range(n):
        totalSum += a[i]
        res += (i * a[i])
        
    maxi = max(maxi, res)
    for i in range(n):
        res = res - (totalSum - a[i]) + (a[i] * (n - 1))
        maxi = max(maxi, res)
        
    return maxi

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(max_sum(arr, n))

# } Driver Code Ends