class Solution:
    def findGreater(self, arr):
        # code here
        from collections import Counter
        n = len(arr)
        ans = [-1]*n
        cnt = Counter(arr)
        stack = []
        for i, e in enumerate(arr):
            while stack and cnt[e] > cnt[arr[stack[-1]]]:
                j = stack.pop()
                ans[j] = arr[i]
            stack.append(i)
        return ans