'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def transformTree(self, root):
        # code here
        s = 0 
        def dfs(node):
            nonlocal s
            if not node:
                return node
            
            dfs(node.right)
            temp= node.data
            node.data = s
            s+=temp
            dfs(node.left)
            return 
        dfs(root)
        return root