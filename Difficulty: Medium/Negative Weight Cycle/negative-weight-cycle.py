class Solution:

    def isNegativeWeightCycle(self, V, edges):
    
        dist = [0] * V
    
        for _ in range(V - 1):
    
            updated = False
    
    
    
            for u, v, w in edges:
    
                if dist[u] + w < dist[v]:
    
                    dist[v] = dist[u] + w
    
                    updated = True
    
    
    
            if not updated:
    
                break
    
    
    
    
    
        for u, v, w in edges:
    
            if dist[u] + w < dist[v]:
    
                return True
    
    
    
        return False