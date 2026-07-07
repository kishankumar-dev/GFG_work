class Solution:
    def largestArea(self, n, m, k, arr):
        # code here
        row=[0,n+1]
        col=[0,m+1]
        for r,c in arr:
            row.append(r)
            col.append(c)
        row.sort()
        col.sort()
        r_max=0
        c_max=0
        for i in range(k+1):
            r_max=max(r_max,row[i+1]-row[i]-1)
            c_max=max(c_max,col[i+1]-col[i]-1)
        return c_max*r_max