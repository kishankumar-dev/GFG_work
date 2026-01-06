class Solution:
    def maxSubarrayXOR(self, arr, k):
        # code here
        n = len(arr)
        if n < k:
            return -1

        window_xor = 0

        # XOR of first window
        for i in range(k):
            window_xor ^= arr[i]

        max_xor = window_xor

        # Sliding window
        for i in range(k, n):
            window_xor ^= arr[i - k]  # remove left element
            window_xor ^= arr[i]      # add new element
            max_xor = max(max_xor, window_xor)

        return max_xor