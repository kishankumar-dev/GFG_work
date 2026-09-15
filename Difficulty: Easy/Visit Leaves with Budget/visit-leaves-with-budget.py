''' Binary Tree Node Structure
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def getCount(self, root, k):
        from collections import deque
        count = 0
        q = deque([(root, 1)])
        while q:
            node, cost = q.popleft()
            is_leaf = True
            for child in (node.left, node.right):
                if child:
                    q.append((child, cost + 1))
                    is_leaf = False
            if is_leaf:
                if cost <= k:
                    count += 1
                    k -= cost
                else:
                    break
        return count