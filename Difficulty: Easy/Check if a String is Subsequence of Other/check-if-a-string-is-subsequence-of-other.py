class Solution:
    def isSubSeq(self, s1, s2):
        # code here
        it = iter(s2)
        return all(ch in it for ch in s1)