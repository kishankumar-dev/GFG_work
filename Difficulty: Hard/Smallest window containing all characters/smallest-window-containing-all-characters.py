class Solution:
    def smallestWindow(self, s, p):
        # code here
        n = len(s)
        freqs = [0] * (ord("z") + 1)
        unique_count = 0
        for c in p:
            ci = ord(c)
            if freqs[ci] == 0:
                unique_count += 1
            freqs[ci] -= 1
        for end in range(n):
            ci = ord(s[end])
            freqs[ci] += 1
            if freqs[ci] == 0:
                unique_count -= 1
                if unique_count == 0:
                    break
        else:
            return ""
        freqs[ord(s[end])] -= 1
        start = min_start = 0
        min_end, min_len = n - 1, n
        for end in range(end, n):
            freqs[ord(s[end])] += 1
            while freqs[c_i := ord(s[start])]:
                freqs[c_i] -= 1
                start += 1
            if (l := end - start + 1) < min_len:
                min_start, min_end, min_len = start, end, l
        return s[min_start:min_end + 1]