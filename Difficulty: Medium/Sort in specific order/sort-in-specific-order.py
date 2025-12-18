class Solution:
    def sortIt(self, arr):
        # code here
        arr.sort(key=lambda x: -x if x&1 else x)
    
