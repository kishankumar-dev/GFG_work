class Solution:
    def countSubs(self, s):
        # code here
        ans = set()
        n = len(s)
        
        for i in range(n):
            for j in range(i+1,n+1):
                ans.add(s[i:j])
        return len(ans)