'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def verticalOrder(self, root): 
        # code here
        if root is None:
            return []
            
        
        from collections import defaultdict, deque
        
        mp = defaultdict(list)
        q = deque()
        
        q.append((root, 0))   # node, horizontal distance
        
        while q:
            node, hd = q.popleft()
            
            mp[hd].append(node.data)
            
            if node.left:
                q.append((node.left, hd - 1))
            
            if node.right:
                q.append((node.right, hd + 1))
        
        ans = []
        
        for key in sorted(mp):
            ans.append(mp[key])
            
        return ans