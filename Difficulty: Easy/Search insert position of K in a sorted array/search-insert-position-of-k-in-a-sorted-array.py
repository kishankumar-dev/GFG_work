class Solution:
    def searchInsertK(self, arr, k):
        # code here
        i=0
        while i<len(arr) and k>arr[i]:
            i+=1
        return i