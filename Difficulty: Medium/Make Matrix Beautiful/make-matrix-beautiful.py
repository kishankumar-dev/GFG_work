class Solution:
    def balanceSums(self, mat):
        # code here 
        max_sum = max(
            # rows
            max(map(sum, mat)),
            # columns
            max(map(sum, zip(*mat)))
        )
        return max_sum * len(mat) - sum(map(sum, mat))