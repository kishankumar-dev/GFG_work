#User function Template for python3

class Solution:
    def longestCommonSubstr(self, str1, str2):
        n, m = len(str1), len(str2)
        lo, hi = 0, min(n, m)+1
        
        def ok(l):
            for i in range(len(str1)-l+1):
                if str2.find(str1[i:i+l]) != -1:
                    return True
            return False
            
        while lo < hi:
            mi = lo+(hi-lo)//2
            if ok(mi):
                lo = mi+1
            else:
                hi = mi
        
        return lo-1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S1 = input().strip()
        S2 = input().strip()
        ob = Solution()
        print(ob.longestCommonSubstr(S1, S2))

# } Driver Code Ends