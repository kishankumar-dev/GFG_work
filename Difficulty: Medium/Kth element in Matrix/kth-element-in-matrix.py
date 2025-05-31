from bisect import bisect_right
class Solution:
    def kthSmallest(self, matrix, k):
        # code here
        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo < hi:
            mid = lo + (hi - lo) // 2
            lte_count = sum(bisect_right(row, mid) for row in matrix)
            if lte_count >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo