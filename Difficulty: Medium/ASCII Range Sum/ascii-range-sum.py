class Solution:
    def asciirange(self, s):
        # code here
        n = len(s)
        dp = [0]*n
        
        acc = 0
        for i, e in enumerate(s):
            acc += ord(e)
            dp[i] = acc
   
        # remember the last occurence position if any
        m = {}
        for i in range(n-1, -1, -1):
            e = s[i]
            if e not in m:
                m[e] = i
        ans = []
        for i, e in enumerate(s):
            if e in m and m[e] - i > 1:
                ans.append(dp[m[e]-1] - dp[i])
                m.pop(e)
        return ans