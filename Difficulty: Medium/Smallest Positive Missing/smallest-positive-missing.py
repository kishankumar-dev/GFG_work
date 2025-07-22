class Solution:
    def missingNumber(self, arr):
        # code here        
        a=set(arr)
        count=1
        while True:
            if count not in a:
                return count
            count+=1