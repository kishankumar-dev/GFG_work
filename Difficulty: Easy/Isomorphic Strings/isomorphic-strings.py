class Solution:
    def areIsomorphic(self, s1, s2):
        # code here 
        d, rev_d = {}, {}
        for a, b in zip(s1, s2):
            if a in d:
                if d[a] != b:
                    return False
            else:
                d[a] = b
                if b in rev_d:
                    if rev_d[b] != a:
                        return False
                else:
                    rev_d[b] = a
        return True