class Solution:  
    def findMaxSum(self,arr):
        # code here
        taken = not_taken = 0
        for a in arr:
            taken, not_taken = not_taken + a, max(taken, not_taken)
        return max(taken, not_taken)

#{ 
 # Driver Code Starts
import sys

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):

        a = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.findMaxSum(a))
        print("~")

# } Driver Code Ends