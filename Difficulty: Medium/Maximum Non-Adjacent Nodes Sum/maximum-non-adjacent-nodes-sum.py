'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def getMaxSum(self, root):
        #code here  
        def dfs(node):
            if node is None:
                return 0, 0
            ltake, lskip = dfs(node.left)
            rtake, rskip = dfs(node.right)
            take = lskip + node.data + rskip
            skip = max(ltake, lskip) + max(rtake, rskip)
            return take, skip
            
        return max(dfs(root))