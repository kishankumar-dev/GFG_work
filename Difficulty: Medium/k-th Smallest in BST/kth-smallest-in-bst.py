'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def kthSmallest(self, root, k): 
        # code here
        if root==None or self.count == k:
            return
        self.kthSmallest(root.left, k)
        self.count += 1
        if self.count  == k:
            self.result = root.data
        self.kthSmallest(root.right, k)    
        return self.result    
    count = 0
    result = -1   