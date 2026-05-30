class Solution:
    def replaceElements(self, arr):
        # code here
        prev = arr[0]
        n = len(arr)
        arr[0] = arr[0]^arr[1]
        for i in range(1,n-1):
            change = prev^arr[i+1]
            prev = arr[i]
            arr[i] = change
        arr[n-1] ^=prev