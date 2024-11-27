#User function Template for python3

class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr):
        #Your code here
        mx = max(arr)
        if mx < 1:
            return 1
        found = [False] * mx
        for val in arr:
            if val > 0 and val <= mx:
                found[val - 1] = True
        for i in range(mx):
            if not found[i]:
                return i + 1
        return mx + 1
 
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.missingNumber(arr))
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends