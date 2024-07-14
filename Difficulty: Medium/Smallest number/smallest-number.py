#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    def smallestNumber(self, s, d):
        # code here
        ans = []
        first = True
        while d > 0:
            start = 1 if first else 0
            first = False
            for i in range(start, 10):
                if 0 <= s-i <= 9*(d-1):
                    ans.append(i)
                    s -= i
                    d -= 1
                    break
            else:
                return -1
        ret = 0
        for e in ans:
            ret = ret*10+e
        return ret
        


#{ 
 # Driver Code Starts.
# Position this line where user code will be pasted.

import sys
import math
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1

for _ in range(t):
    s = int(data[index])
    d = int(data[index + 1])
    index += 2
    ob = Solution()
    print(ob.smallestNumber(s, d))

# } Driver Code Ends