class Solution:
	def maxSumIS(self, arr):
		# code here
		sorted_vals = sorted(set(arr))
        comp = {v: i+1 for i, v in enumerate(sorted_vals)}  # 1-based index

        # Fenwick Tree for range max queries
        size = len(sorted_vals)
        BIT = [0] * (size + 1)

        def update(idx, val):
            while idx <= size:
                BIT[idx] = max(BIT[idx], val)
                idx += idx & -idx

        def query(idx):
            res = 0
            while idx > 0:
                res = max(res, BIT[idx])
                idx -= idx & -idx
            return res

        ans = 0
        for x in arr:
            idx = comp[x]
            best_before = query(idx - 1)   # best sum for smaller values
            curr_sum = best_before + x
            update(idx, curr_sum)
            ans = max(ans, curr_sum)

        return ans