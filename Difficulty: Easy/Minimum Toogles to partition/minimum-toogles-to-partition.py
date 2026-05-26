class Solution:
    def minToggle(self, arr):
        # code here
        n = len(arr)
        suffix_zeros = arr.count(0)
        prefix_ones = 0
        min_toggles = suffix_zeros
        for last_zero_i in range(n):
            if arr[last_zero_i]:
                prefix_ones += 1
            else:
                suffix_zeros -= 1
                if (t := prefix_ones + suffix_zeros) < min_toggles:
                    min_toggles = t
        return min_toggles