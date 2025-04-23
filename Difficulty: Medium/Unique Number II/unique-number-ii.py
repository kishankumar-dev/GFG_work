#User function Template for python3

class Solution:
	def singleNum(self, arr):
		# Code here
		ans = []
		count = {}
        for i in arr:
            count[i] = count.get(i, 0) + 1
        for key in count:
            if count[key] == 1:
                ans.append(key)
        return sorted(ans)


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))

        ob = Solution()
        ans = ob.singleNum(arr)

        print(" ".join(map(str, ans)))
        tc -= 1
        print("~")

# } Driver Code Ends