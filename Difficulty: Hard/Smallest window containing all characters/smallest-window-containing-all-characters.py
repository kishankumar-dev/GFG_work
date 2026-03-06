from collections import Counter
class Solution:
    def minWindow(self, s, p):
        # code here
        if len(p) > len(s):
            return ""

        p_count = Counter(p)
        window = {}
        
        have = 0
        need = len(p_count)
    
        res = [-1, -1]
        min_len = float("inf")
    
        left = 0
    
        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1
    
            if char in p_count and window[char] == p_count[char]:
                have += 1
    
            while have == need:
                
                if (right - left + 1) < min_len:
                    res = [left, right]
                    min_len = right - left + 1
    
                window[s[left]] -= 1
    
                if s[left] in p_count and window[s[left]] < p_count[s[left]]:
                    have -= 1
    
                left += 1
    
        l, r = res
        return s[l:r+1] if min_len != float("inf") else ""