class Solution:
    def findUnique(self, arr):
        # code here 
        count = {}
        for i in arr:
            count[i] = count.get(i, 0) + 1
        for key in count:
            if count[key] == 1:
                return key

#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.findUnique(arr)
        print(ans)
        print("~")
# } Driver Code Ends