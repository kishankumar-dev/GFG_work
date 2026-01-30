class Solution:
    def rearrangeQueue(self, q):
        #code here  
        n = len(q)
        half = n // 2
        
        temp = deque()
        
        # Step 1: move first half to temp queue
        for _ in range(half):
            temp.append(q.popleft())
        
        # Step 2: interleave elements
        while temp:
            q.append(temp.popleft())  
            q.append(q.popleft())  