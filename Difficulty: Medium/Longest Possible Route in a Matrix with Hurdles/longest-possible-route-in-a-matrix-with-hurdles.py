class Solution:
    def longestPath(self, mat, xs, ys, xd, yd):
        # code here
        if mat[xs][ys]==0 or mat[xd][yd]==0: return -1
        n,m=len(mat),len(mat[0])
        ans=-1

        def dfs(x,y,d):
            nonlocal ans
            if (x,y)==(xd,yd):
                ans=max(ans,d)
                return
            mat[x][y]=0
            for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nx,ny=x+dx,y+dy
                if 0<=nx<n and 0<=ny<m and mat[nx][ny]:
                    dfs(nx,ny,d+1)
            mat[x][y]=1

        dfs(xs,ys,0)
        return ans