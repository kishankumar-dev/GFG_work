#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


# } Driver Code Ends
#User function Template for python3
from typing import List

class Solution:
    def countPairs(self, arr: List[int], target: int) -> int:
        freq = {}
        ans = 0
        for ai in arr:
            aj = target - ai
            if aj in freq:
                ans += freq[aj]
            if ai in freq:
                freq[ai] += 1
            else:
                freq[ai] = 1
        return ans

#{ 
 # Driver Code Starts.

def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        k = int(input())
        ob = Solution()
        print(ob.countPairs(A, k))
        print('~')
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends