class Solution:
    def generateBinary(self, n):
        # code here
        return [bin(i)[2:] for i in range(1,n+1)]
        