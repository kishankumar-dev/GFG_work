class Solution:
    def countPaths(self, edges, V, src, dest):
        #Code here        
        from collections import defaultdict
        adj=defaultdict(set)
        for sta,sto in edges:
            adj[sta].add(sto)
        from functools import lru_cache
        @lru_cache(None)
        def dfs(cur=src):
            if cur==dest:
                return 1
            tot=0
            for nxt in adj[cur]:
                tot+=dfs(nxt)
            return tot
        return dfs()