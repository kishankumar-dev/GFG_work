class Solution:
    def reverseQueue(self, q):
        # code here
        if not q:
            return q
        
        front = q.popleft()
        
        self.reverseQueue(q)
        
        q.append(front)
        
        return q