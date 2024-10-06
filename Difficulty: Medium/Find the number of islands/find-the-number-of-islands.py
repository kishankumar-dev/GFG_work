#User function Template for python3

class Solution:
    
    rowDir = [-1, -1, -1, 0, 0, 1, 1, 1]
    colDir = [-1, 0, 1, -1, 1, -1, 0, 1]
    
    def numIslands(self, grid):
        if not grid or len(grid) == 0:
            return 0
        
        ans = 0
        n = len(grid)
        m = len(grid[0])
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    ans += 1
                    self.dfs(grid, i, j)
        return ans
        
    def dfs(self, grid, row, col):
        stack = [(row, col)]
        grid[row][col] = 0
        
        while stack:
            r, c = stack.pop()
            
            
            for d in range(8):
                new_r = r + self.rowDir[d]
                new_c = c + self.colDir[d]
                
                if self.isValid(grid, new_r, new_c) and grid[new_r][new_c] == 1:
                    grid[new_r][new_c] = 0
                    stack.append((new_r, new_c))
                    
    def isValid(self, grid, row, col):
        return 0 <= row < len(grid) and 0 <= col < len(grid[0])

#{ 
 # Driver Code Starts
# Driver code
if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().strip().split())
        grid = []
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj = Solution()
        print(obj.numIslands(grid))

# } Driver Code Ends