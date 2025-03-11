
class Solution:
    def countWays(self, n):
        # code here
        n0, n1 = 0, 1
        for i in range(1, n+1):
            n0, n1 = n1, n1+n0
        return n1

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

sys.setrecursionlimit(10**6)

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m = int(input())
        ob = Solution()
        print(ob.countWays(m))

        print("~")

# } Driver Code Ends