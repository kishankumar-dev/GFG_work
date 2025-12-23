from bisect import bisect_left as bl, bisect_right as br
class Solution:
    def cntInRange(self, arr, queries):
        # code here
        arr.sort()
        return [br(arr, r)- bl(arr, l) for l, r in queries]