class Solution:
    def increasingNumbers(self, n):
        # code here
        def solve(tot_digi,curent,num,ans):
            if tot_digi==0:
                ans.append(num)
            
            for i in range(curent+1,10):
                solve(tot_digi-1,i,(num*10)+i,ans)
            
            
        ans=[]
        if n==1:
            ans.append(0)
        for i in range(1,10):
            solve(n-1,i,i,ans)
        return ans
