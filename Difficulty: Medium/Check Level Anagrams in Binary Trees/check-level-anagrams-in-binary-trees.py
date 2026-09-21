"""
Structure of binary tree Node
class Node:
    def __init__(self, x: int):
        self.data = x
        self.left = self.right = None
"""


class Solution:

    def areAnagrams(self, root1, root2):
        """ code here """
        from collections import deque, defaultdict
        q1, q2 = deque([root1]), deque([root2])
        while q1 and q2:
            freqs = defaultdict(int)
            for q, v in [(q1, 1), (q2, -1)]:
                for _ in range(len(q)):
                    node = q.popleft()
                    if node:
                        freqs[node.data] += v
                        q.extend((node.left, node.right))
            if any(freqs.values()):
                return False
        return q1 == q2