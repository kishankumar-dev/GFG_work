class Solution:
	def countPairs(self, mat1, mat2, x):
		# code here        
		a=[]
        b=[]
        count=0
        rows=len(mat1)
        cols=len(mat1[0])
        a = [mat1[j][i] for i in range(cols) for j in range(rows)]
        b = [mat2[j][i] for i in range(cols) for j in range(rows)]
        b_set = set(b)
        for i in a:
          if (x-i) in b_set:
               count+=1
        return count