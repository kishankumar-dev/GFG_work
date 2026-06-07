class Solution:
    def profession(self, level, pos):
        # code here
        def dfs(lv,ps):
            if ps<2:
                return ps
            return dfs(lv-1,(ps+1)//2) if ps%2==1 else 1-dfs(lv-1,ps//2)
        return "Engineer" if dfs(level, pos) == 1 else "Doctor"