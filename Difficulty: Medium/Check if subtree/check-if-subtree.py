class Solution:
    def isIdentical(self, a, b):
        if not a and not b: return True
        if not a or not b: return False
        return a.data == b.data and self.isIdentical(a.left, b.left) and self.isIdentical(a.right, b.right)

    def isSubTree(self, t, s):
        if not s: return True
        if not t: return False
        return self.isIdentical(t, s) or self.isSubTree(t.left, s) or self.isSubTree(t.right, s)