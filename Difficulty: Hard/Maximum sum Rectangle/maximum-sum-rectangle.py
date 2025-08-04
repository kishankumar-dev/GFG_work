from itertools import accumulate
class Solution:
    def maxRectSum(self, mat):
        # code here
        m, n = len(mat), len(mat[0])
        arr = [list(accumulate(r)) for r in mat]
        
        ans = float('-inf')
        for c1 in range(n):     
            for c2 in range(c1, n): 
                area = 0
                for r in range(m): 
                    area += arr[r][c2]   
                    if c1-1 >= 0:
                        area -= arr[r][c1-1]
                    ans = max(ans, area)
                    area = max(area, 0)
        return ans