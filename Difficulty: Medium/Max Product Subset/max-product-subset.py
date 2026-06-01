class Solution:
    def findMaxProduct(self, arr):
        # code here
        MOD = 1000000007
        n = len(arr)

        if n == 1:
            return arr[0]

        neg_count = 0
        zero_count = 0
        product = 1
        max_negative = -11  
        # negative closest to zero

        for x in arr:
            if x == 0:
                zero_count += 1
                continue

            if x < 0:
                neg_count += 1
                max_negative = max(max_negative, x)

            product *= x

        # all zeros
        if zero_count == n:
            return 0

        # only one negative and all others zero
        if neg_count == 1 and neg_count + zero_count == n:
            return 0

        # odd negatives -> remove the negative with smallest abs value
        if neg_count % 2:
            product //= max_negative

        return product % MOD