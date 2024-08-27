class Solution:
    def findMaxDiff(self, arr):
        # code here
        s, left_smallers = [], []
        for a in arr:
            while s and s[-1] >= a:
                s.pop()
            left_smallers.append(s[-1] if s else 0)
            s.append(a)
        s.clear()
        maxi = 0
        for i in reversed(range(len(arr))):
            a = arr[i]
            while s and s[-1] >= a:
                s.pop()
            right_smaller = s[-1] if s else 0
            maxi = max(maxi, abs(left_smallers[i] - right_smaller))
            s.append(a)
        return maxi

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.findMaxDiff(arr))

# } Driver Code Ends