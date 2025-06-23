import sys

sys.set_int_max_str_digits(10**7) 

class Solution:
    def minSum(self, arr):
        arr = list(filter(lambda x: x != 0, arr))
        arr.sort()
        n = len(arr)
        i, j = 0, 1

        a = ''
        b = ''

        while i < n and j < n:
            a += str(arr[i])
            b += str(arr[j])
            i += 2
            j += 2
            
        if i < n:
            a += str(arr[i])
            
        return int(a) + (int(b) if b != '' else 0)