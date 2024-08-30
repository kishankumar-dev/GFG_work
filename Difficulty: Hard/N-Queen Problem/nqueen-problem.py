#User function Template for python3

class Solution:
    def nQueen(self, n):
        # code here
        ans = []
        def queen(board, r):
            if r == n:
                ans.append(board[:])
                return
            for c in range(1, n+1):
                board.append(c)
                for p in range(r):
                    if board[p] == c or abs(board[p]-c) == abs(r-p):
                        break
                else:
                    queen(board, r+1)
                board.pop()
        
        queen([], 0)
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        ans = ob.nQueen(n)
        if(len(ans) == 0):
            print("-1")
        else:
            for i in range(len(ans)):
                print("[",end="")
                for j in range(len(ans[i])):
                    print(ans[i][j],end = " ")
                print("]",end = " ")
            print()
                
# } Driver Code Ends