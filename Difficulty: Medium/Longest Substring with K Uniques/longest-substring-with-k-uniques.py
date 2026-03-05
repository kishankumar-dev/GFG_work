class Solution:
    def longestKSubstr(self, s, k):
        # code here
        mx=-1
        from collections import Counter
        cnt=Counter()
        left=0
        for right,ve in enumerate(s):
            cnt[ve]+=1
            while len(cnt)>k:
                cnt[s[left]]-=1
                if cnt[s[left]]==0:
                    del cnt[s[left]]
                left+=1
            if len(cnt)==k:
                mx=max(mx,right-left+1)
        return mx
        