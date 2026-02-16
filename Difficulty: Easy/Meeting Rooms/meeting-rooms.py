class Solution:
    def canAttend(self, arr):
        # Code Here
        arr.sort()
        return all(arr[i][1] <= arr[i + 1][0] for i in range(len(arr) - 1))