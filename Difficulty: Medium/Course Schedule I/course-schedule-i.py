class Solution:
    def canFinish(self, n, prerequisites):
        # code here 
        adjList = [[] for _ in range(n)]
        indegree = [0]*n
        for v, u in prerequisites:
            adjList[v].append(u)
            indegree[u] += 1
            
        queue = deque([i for i in range(n) if indegree[i] == 0])
        while queue:
            src = queue.popleft()
            
            for nbr in adjList[src]:
                indegree[nbr] -= 1
                if indegree[nbr] == 0:
                    queue.append(nbr)
        
        for i in range(n):
            if indegree[i] != 0:
                return False
        return True