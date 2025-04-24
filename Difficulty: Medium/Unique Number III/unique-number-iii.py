#User function Template for python3

class Solution:
    def getSingle(self, arr):
        # code here 
        map = dict()
        for i in arr:
            if i in map:
                map[i] += 1
            else:
                map[i] = 1
        for i, j in map.items():
            if j == 1:
                return i

#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSingle(arr)
        print(ans)
        print("~")
# } Driver Code Ends