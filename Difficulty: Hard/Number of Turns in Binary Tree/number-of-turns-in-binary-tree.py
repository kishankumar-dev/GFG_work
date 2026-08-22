''' Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:

    def findLCA(self, root, p, q):
        if not root or root.data == p or root.data == q:
            return root
    
        leftLCA = self.findLCA(root.left, p, q)
        rightLCA = self.findLCA(root.right, p, q)
    
        if leftLCA and rightLCA:
            return root
    
        return leftLCA if leftLCA else rightLCA
    
    def getPath(self, root, target, path):
        if not root:
            return False
    
        if root.data == target:
            return True
    
        path.append('L')
        if self.getPath(root.left, target, path):
            return True
        path.pop()
    
        path.append('R')
        if self.getPath(root.right, target, path):
            return True
        path.pop()
    
        return False
    
    def countTurns(self, path):
        turns = 0
    
        for i in range(len(path) - 1):
            if path[i] != path[i + 1]:
                turns += 1
    
        return turns
    
    def numberOfTurns(self, root, p, q):
        if not root or p == q:
            return -1
    
        lca = self.findLCA(root, p, q)
    
        if not lca:
            return -1
    
        # LCA is p: only need the path from p to q.
        if lca.data == p:
            path = []
            self.getPath(lca, q, path)
    
            turns = self.countTurns(path)
            return -1 if turns == 0 else turns
    
        # LCA is q: only need the path from q to p.
        if lca.data == q:
            path = []
            self.getPath(lca, p, path)
    
            turns = self.countTurns(path)
            return -1 if turns == 0 else turns
    
        # LCA is neither p nor q.
        pathToP = []
        pathToQ = []
    
        self.getPath(lca, p, pathToP)
        self.getPath(lca, q, pathToQ)
    
        # The +1 is the turn at the LCA.
        turns = (
            self.countTurns(pathToP)
            + self.countTurns(pathToQ)
            + 1
        )
    
        return -1 if turns == 0 else turns