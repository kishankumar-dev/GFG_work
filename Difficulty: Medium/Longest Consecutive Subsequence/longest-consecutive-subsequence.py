 #User function Template for python3
 
class Solution:
    
    # arr[] : the input array
    
    #Function to return length of longest subsequence of consecutive integers.
    def longestConsecutive(self,arr):
        #code here
        n = len(arr)
        if n == 0:
            return 0  # Edge case: If the array is empty
        
        arr.sort()
        count = 1
        result = 1
        
        for i in range(1, n):
            if arr[i] == arr[i - 1]:
                continue  # Skip duplicate elements
            if arr[i] - 1 == arr[i - 1]:
                count += 1
            else:
                result = max(result, count)
                count = 1
        
        result = max(result, count)  # Check the last subsequence
        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        a = list(map(int, input().strip().split()))
        print(Solution().longestConsecutive(a))
        print("~")
# } Driver Code Ends