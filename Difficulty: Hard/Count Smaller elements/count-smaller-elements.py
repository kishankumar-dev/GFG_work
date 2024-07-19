#User function Template for python3
import bisect
class Solution:

	def constructLowerArray(self,arr):
		# code here
		ans=[0]
        right=[arr[-1]]
        for i in range(len(arr)-2,-1,-1):
            count=bisect.bisect_left(right,arr[i])
            bisect.insort(right,arr[i])
            ans.append(count)
        return ans[::-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.constructLowerArray(arr)
        for x in ans:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends