class Solution:
    def countConsec(self, n: int) -> int:
        # code here 
        zeros, ones = 1, 1
        for i in range(2, n+1):
            zeros, ones = zeros + ones, zeros
        return 2**n - zeros - ones