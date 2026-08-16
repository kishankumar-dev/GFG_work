class Solution:
    def minProd(self, arr):
        # code here
        n = len(arr)
        if n == 1:
            return arr[0]
        mini, max_neg, prod = 11, -11, 1
        for i in range(n):
            if arr[i] < mini:
                mini = arr[i]
            if arr[i]:
                prod *= arr[i]
                if max_neg < arr[i] < 0:
                    max_neg = arr[i]
        if mini >= 0:
            return mini
        elif prod < 0:
            return prod
        else:
            return prod // max_neg
