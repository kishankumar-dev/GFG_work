class Solution:
    def longestSubarray(self, arr):
        # code here
        n = len(arr)
        if n == 0:
            return 0

        # bucket indices by value clamped to [0..n]
        buckets = [[] for _ in range(n + 1)]
        for i, v in enumerate(arr):
            if v < 0:
                buckets[0].append(i)       # treat negatives as 0
            elif v <= n:
                buckets[v].append(i)      # only values <= n matter
            # values > n are impossible to satisfy (len <= n < value)

        parent = list(range(n))
        size = [1] * n
        active = [False] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return ra
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]
            return ra

        ans = 0
        max_comp = 0

        # process thresholds from 0..n (activate indices with value == threshold)
        for x in range(0, n + 1):
            for pos in buckets[x]:
                active[pos] = True
                # union with left neighbor if active
                if pos - 1 >= 0 and active[pos - 1]:
                    union(pos, pos - 1)
                # union with right neighbor if active
                if pos + 1 < n and active[pos + 1]:
                    union(pos, pos + 1)
                # update max component size
                root = find(pos)
                if size[root] > max_comp:
                    max_comp = size[root]

            # only meaningful for lengths >= 1
            if x >= 1 and max_comp >= x:
                # a component of size max_comp (with all values <= x) satisfies max ≤ x ≤ size
                if max_comp > ans:
                    ans = max_comp

        return ans