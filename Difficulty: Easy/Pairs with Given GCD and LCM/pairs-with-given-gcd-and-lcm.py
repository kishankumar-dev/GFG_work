class Solution:
    def pairCount(self, x, y):
        import math
        d, r = divmod(y, x)
        # d - the distinct prime factors
        if r:  # invalid gcm & lcm pair
            return 0
        p_count = 0  # distinct prime factors count
        for f in range(2, math.isqrt(d) + 1):
            present = False
            while (qr := divmod(d, f))[1] == 0:
                present = True
                d = qr[0]
            if present:
                p_count += 1
        if d > 1:  # single prime factor
            p_count += 1
        return 1 << p_count