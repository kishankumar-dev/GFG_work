class Solution:
	def andInRange(self, l, r):
		# code here
		num2=bin(r)[2:]
	    num1=bin(l)[2:].zfill(len(num2))
	    i=0
	    while i<len(num1) and num1[i]==num2[i]:
	        i+=1
	    res=0
	    mul=2**(len(num1)-i)
	    for j in range(i-1,-1,-1):
	        if num1[j]=='1':
    	        res+=mul
    	    mul*=2
    	return res
