class Solution:
    def nextLargerElement(self, arr):
        # code here
        from itertools import chain
        n = len(arr)
        nge = [-1] * n
        s = []
        for i in chain(range(n), range(n)):
            while s and arr[s[-1]] < arr[i]:
                j = s.pop()
                nge[j] = arr[i]
            s.append(i)
        return nge