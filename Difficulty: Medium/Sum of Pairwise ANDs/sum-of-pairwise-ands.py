class Solution:
    def pairAndSum(self, arr):
        ans = 0

        # Check each bit separately.
        # If a bit is set in k elements, then that bit will be
        # present in the AND of kC2 pairs.
        for bit in range(31):
            count = 0

            # Count how many numbers have the current bit set.
            for x in arr:
                if x & (1 << bit):
                    count += 1

            # Number of pairs having this bit set in AND.
            pairs = count * (count - 1) // 2

            # Add contribution of this bit to the answer.
            ans += pairs * (1 << bit)

        return ans