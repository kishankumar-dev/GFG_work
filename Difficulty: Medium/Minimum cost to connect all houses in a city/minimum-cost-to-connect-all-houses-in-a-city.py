#User function Template for python3
class Solution:
    def minCost(self, houses):
      # code here
        distance = lambda i, j: abs(houses[i][0]-houses[j][0]) + abs(houses[i][1]-houses[j][1])
            
        if len(houses) == 1:
            return 0
        
        edges = []
        for i in range(len(houses)-1):
            for j in range(i+1, len(houses)):
                edges.append((i, j, distance(i, j)))
        edges.sort(key = lambda d: d[2])
        
        parents = list(range(len(houses)))
        
        def find(u):
            if parents[u] != u:
                parents[u] = find(parents[u])
            return parents[u]
        
        costs = 0
        for u, v, d in edges:
            ru = find(u)
            rv = find(v)
            if ru != rv:
                parents[ru] = rv
                costs += d
        return costs

#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        edges = []

        for _ in range(n):
            temp = list(map(int, input().split()))
            edges.append(temp)

        obj = Solution()
        print(obj.minCost(edges))
        print("~")
# } Driver Code Ends