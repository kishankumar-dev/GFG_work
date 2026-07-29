class Solution:
    def minSubsets(self, arr):
        arr.sort()
        pos = res = 1
        for i in arr[1:]:
            res += int( arr[pos] != arr[pos-1] + 1 )
            pos += 1
        return res