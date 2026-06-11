class Solution:
    def findIndex(self, s):
        # code here 
        closed_count = s.count(")")
        open_count = 0
        for i, c in enumerate(s):
            if open_count == closed_count:
                return i
            if c == "(":
                open_count += 1
            else:
                closed_count -= 1
        return len(s)