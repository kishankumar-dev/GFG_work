''' Structure of Binary Tree Node
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def maxDiff(self, root):
        if not root:
            return

       # local function to find max_diff value recursively
        def set_max_diff(node, max_ancestor):
            if not node:
                return

            nonlocal max_diff
            nonlocal root

           # skip calculating max_diff for root because at root max_ancestor is root.data and root.data - root.data = 0; it is impacting negative reuslts
            max_diff = max(max_diff, max_ancestor - node.data) if node != root else float('-inf')
            max_ancestor = max(max_ancestor, node.data)
            set_max_diff(node.left, max_ancestor)
            set_max_diff(node.right, max_ancestor)


        max_diff = float('-inf')
        max_ancestor = root.data
        set_max_diff(root, max_ancestor)

        return max_diff
        