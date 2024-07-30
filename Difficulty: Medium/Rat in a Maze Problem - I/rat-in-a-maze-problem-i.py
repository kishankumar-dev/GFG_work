from typing import List

class Solution:
    def findPath(self, m: List[List[int]]) -> List[str]:
        # code here
        ans, visited, n = [], set(), len(m)
        def dfs(r, c, dirs):
            nonlocal ans, visited
            if r < 0 or r >= n or c < 0 or c >= n or m[r][c] == 0 or (r, c) in visited:
                return 
            
            if (r, c) == (n-1, n-1):
                ans.append("".join(dirs))
                return
            
            visited.add((r, c))
            for d in "UDLR":
                dirs.append(d)
                if d == 'U':
                    dfs(r-1, c, dirs)
                if d == 'D':
                    dfs(r+1, c, dirs)
                if d == 'L':
                    dfs(r, c-1, dirs)
                if d == 'R':
                    dfs(r, c+1, dirs)
                dirs.pop()
            visited.remove((r, c))
        dfs(0, 0, [])
        return ans if ans else ["-1"]

#{ 
 # Driver Code Starts
# Main function to read input and output the results
if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        m = []
        for i in range(n):
            m.append(list(map(int, input().strip().split())))
        obj = Solution()
        result = obj.findPath(m)
        result.sort()
        if len(result) == 0:
            print(-1)
        else:
            print(" ".join(result))

# } Driver Code Ends