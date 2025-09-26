from collections import deque
class Solution:    
    def rotateDeque(self, dq, type, k):
        l = len(dq)
        k = k % l
        if type == 1:
            dq.rotate(k)
        else:
            dq.rotate(-k)