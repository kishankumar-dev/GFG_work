class Solution:
    def isBridge(self, V, edges, c, d):
        # code here 
        if c in adj[d]:
            adj[d].remove(c)
        if d in adj[c]:
            adj[c].remove(d)
        else:
            return 0
        def dfs(node):
            visit.add(node)
            for ngh in adj[node]:
                if ngh not in visit:
                    dfs(ngh)
        visit = set()
        dfs(c)
        if d in visit:
            return 0
        return 1


#{ 
 # Driver Code Starts
import sys

sys.setrecursionlimit(10**7)
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        V = int(input())
        E = int(input())
        adj = [[] for _ in range(V)]
        edges = []

        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
            edges.append([u, v])

        c = int(input())
        d = int(input())

        obj = Solution()
        l = obj.isBridge(V, edges, c, d)

        if l:
            print("true")
        else:
            print("false")

        print("~")

# } Driver Code Ends