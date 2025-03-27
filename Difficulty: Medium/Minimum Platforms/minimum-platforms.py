#User function Template for python3

class Solution:    
    def minimumPlatform(self,arr,dep):
        trains = sorted([(v, 1) for v in arr] + [(v+1, -1) for v in dep])
        ans, platform = 0, 0
        for _, t in trains:
            platform += t
            ans = max(ans, platform)
        return ans
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        arrival = list(map(int, input().strip().split()))
        departure = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.minimumPlatform(arrival, departure))
        print("~")

# } Driver Code Ends