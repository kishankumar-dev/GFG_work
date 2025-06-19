class Solution:
    def caseSort(self,s):
        #code here        
        up = ""
        lo = ""
        
        for i in s:
            if(ord(i) <= 90):
                up += i
            else:
                lo += i
        
        up = sorted(up)
        lo = sorted(lo)
        
        i = 0
        j = 0
        
        ans = str()
        for k in s:
            if(ord(k) <= 90):
                ans += up[i]
                i += 1
            else:
                ans += lo[j]
                j += 1
        
        return ans