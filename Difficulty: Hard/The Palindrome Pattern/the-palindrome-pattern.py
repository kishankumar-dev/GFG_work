#User function Template for python3
class Solution:
    def flipR(self,arr,i):
        return list(reversed(arr[i]))
    def flipC(self,arr,j):
        n=len(arr)
        return [arr[n-k-1][j] for k in range(n)]
    def pattern (self, arr):
        if len(arr)==1:
            return "0 R"
        n=len(arr)
        for i in range(n):
            if self.flipR(arr,i)==arr[i]:
                return str(i)+" R"
        for i in range(n):
            if self.flipC(arr,i)==[arr[j][i] for j  in range(n)]:
                return str(i)+" C"
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        a = list()
        c = 0
        for i in range(0, n):
            X = list()
            for j in range(0, n):
                X.append(arr[c])
                c += 1
            a.append(X)
        ans = ob.pattern(a)
        print(ans)

# } Driver Code Ends