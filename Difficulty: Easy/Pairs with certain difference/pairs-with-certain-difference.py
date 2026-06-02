class Solution:
    def sumDiffPairs(self, arr, k):
        # code here
        n = len(arr)
        arr = sorted(arr, reverse = True)
        if n < 2:
            return 0
          
        i = 0
        j = 1
        total = 0
        while j < n:
            if arr[i] - arr[j] < k:
                total += (arr[i] + arr[j])
                i += 2
                j += 2
            else:
                i += 1
                j += 1
          
        return total