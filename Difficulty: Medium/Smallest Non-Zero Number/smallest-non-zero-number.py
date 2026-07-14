class Solution:
    def find(self, arr):
        from functools import reduce
        return reduce(lambda x, a: (x + a + 1) // 2, reversed(arr), 0)