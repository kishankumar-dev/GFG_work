from collections import Counter
class Solution:
    def countAtMostK(self, arr, k):
        # Code here
        cnt = Counter()
        left, ans = 0, 0
        for r, e in enumerate(arr):
            cnt[e] += 1
            while left <= r and len(cnt) > k:
                cnt[arr[left]] -= 1
                if cnt[arr[left]] == 0:
                    cnt.pop(arr[left])
                left += 1
            ans += (r-left+1)
        return ans