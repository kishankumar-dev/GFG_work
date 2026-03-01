class Solution:
	def pushZerosToEnd(self, arr):
        # code here
        i=0
        for x in arr:
            if x!=0:
                arr[i]=x
                i+=1
        while i<len(arr):
            arr[i]=0
            i+=1
        return arr