#User function Template for python3

class Solution:
    def nearlySorted(self, a, k):
        #code
        import heapq
        def elements(a, k):
            h = a[:k]
            heapq.heapify(h)
        
            for e in a[k:]:
                yield heapq.heappushpop(h, e)
                
            while h:
                yield heapq.heappop(h)
        
        for i, e in enumerate(elements(a, k)):
            a[i] = e
        return a

#{ 
 # Driver Code Starts
# Initial Template for Python 3
# Position this line where user code will be pasted.
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        k = int(input())
        ob = Solution()
        ob.nearlySorted(arr, k)
        print(*arr)
        print("~")
        t -= 1
# } Driver Code Ends