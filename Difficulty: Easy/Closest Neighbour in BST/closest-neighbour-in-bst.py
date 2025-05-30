'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findMaxFork(self, root, k):
        ret=None
        def dfs(cur=root):
            nonlocal k,ret
            if not cur:
                return
            if cur.data<=k:
                ret=cur.data
                dfs(cur.right)
                return
            dfs(cur.left)
        dfs()
        return ret if ret!=None else -1