#User function Template for python3

class Solution:
    def findMin(self, arr):
        #complete the function here
        n = len(arr)
        while n-1 >= 0 and arr[n-1] == arr[0]:
            n -= 1
        if n == 0:
            return arr[0]
            
        lo, hi = 0, n
        while lo < hi:
            mi = lo+(hi-lo)//2
            if arr[mi] < arr[0]:
                hi = mi
            else:
                lo = mi+1
        
        return arr[0] if lo == n else arr[lo]


#{ 
 # Driver Code Starts
def main():
    T = int(input())

    while T > 0:
        a = list(map(
            int,
            input().strip().split()))  # Convert input to list of integers
        print(Solution().findMin(a))  # Call findMin with the array 'a'
        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends