from collections import defaultdict
class Solution:
    def diameter(self, V, edges):
        # Code here
        adj=defaultdict(set)
        for sta,sto in edges:
            adj[sta].add(sto)
            adj[sto].add(sta)
        ret=[0,-1]
        def dfs(cur=0,prv=None,dis=0):
            nonlocal adj,ret
            ret=max(ret,[dis,cur])
            for nxt in adj[cur]:
                if nxt==prv:
                    continue
                dfs(nxt,cur,dis+1)
        dfs()
        sta=ret[1]
        ret=[0,-1]
        dfs(sta)
        return ret[0]