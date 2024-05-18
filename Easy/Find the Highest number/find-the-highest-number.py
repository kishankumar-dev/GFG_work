#User function Template for python3
from typing import List

class Solution:
	def findPeakElement(self, a):
		# Code here
		l, r = 0, len(a)-1
		while l < r:
		    m = l + (r-l)//2
		    if a[m] < a[m+1]:
		        l = m + 1
		    else:
		        r = m
	    return a[l]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        a = list(map(int, input().split()))
        ob = Solution()
        ans = ob.findPeakElement(a)
        print(ans)

# } Driver Code Ends