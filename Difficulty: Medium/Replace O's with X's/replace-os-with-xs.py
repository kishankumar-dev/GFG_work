from collections import deque
class Solution:
    def fill(self, grid):
        q=deque([])
        vis=set()
        for i in range(len(grid)):
            if grid[i][0]=='O':
                q.append((i,0))
                vis.add((i,0))
            if grid[i][-1]=='O':
                q.append((i,len(grid[0])-1))
                vis.add((i,len(grid[0])-1))
        for j in range(len(grid[0])):
            if grid[0][j]=='O':
                q.append((0,j))
                vis.add((0,j))
            if  grid[-1][j]=='O':
                q.append((len(grid)-1,j))
                vis.add((len(grid)-1,j))
        d=[[0,-1],[0,1],[-1,0],[1,0]]
        
        while q:
            i,j=q.popleft()
            for k in d:
                x,y=i+k[0],j+k[1]
                if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y]=='O' and (x,y) not in vis:
                    vis.add((x,y))
                    q.append((x,y))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='O' and (i,j) not in vis:
                    grid[i][j]='X'
        return grid