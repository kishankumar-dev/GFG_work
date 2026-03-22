class Solution:
	def orangesRot(self, mat):
		# code here
        hth=len(mat)
        wth=len(mat[0])
        cnt=sum(rw.count(1) for rw in mat)
        if cnt==0:
            return 0
        t=0
        q=[(x,y,) for x in range(wth) for y in range(hth) if mat[y][x]==2]
        while q:
            nq=[]
            for x,y in q:
                mat[y][x]=0
                for dx,dy in [(0,1,),(0,-1,),(1,0,),(-1,0,),]:
                    nx=x+dx
                    ny=y+dy
                    if not(0<=nx<wth and 0<=ny<hth):
                        continue
                    if mat[ny][nx]!=1:
                        continue
                    mat[ny][nx]=2
                    nq.append((nx,ny,))
                    cnt-=1
            q=nq
            t+=1
            if cnt==0:
                return t
        return -1

