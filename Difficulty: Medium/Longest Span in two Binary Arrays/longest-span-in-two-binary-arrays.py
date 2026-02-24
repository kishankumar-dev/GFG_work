class Solution:
    def equalSumSpan(self, a1, a2):
        # code here
        n = len(a1)
        
        # Dictionary to store first occurrence of diff
        diff_map = {}
        
        prefix1 = 0
        prefix2 = 0
        max_len = 0
        
        for i in range(n):
            prefix1 += a1[i]
            prefix2 += a2[i]
            
            curr_diff = prefix1 - prefix2
            
            # If diff is 0, span is from 0 to i
            if curr_diff == 0:
                max_len = i + 1
            
            # If diff seen before
            elif curr_diff in diff_map:
                max_len = max(max_len, i - diff_map[curr_diff])
            
            # Store first occurrence of diff
            else:
                diff_map[curr_diff] = i
        
        return max_len