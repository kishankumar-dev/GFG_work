from itertools import pairwise
class Solution:
    def maxSum(self, arr):
        # code here
        return max(map(sum, pairwise(arr)))
