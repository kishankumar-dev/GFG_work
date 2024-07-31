from functools import reduce
class Solution:
    def calculate_prefix(self, x, y):
        prefix = ""
        for i in range(min(len(x), len(y))):
            if x[i] == y[i]:
                prefix += x[i]
            else:
                break
        return prefix
        
    def longestCommonPrefix(self, arr):
        if not arr:
            return "-1"
        ans = reduce(lambda x, y: self.calculate_prefix(x, y), arr)
        return "-1" if ans == "" else ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        arr = [x for x in input().strip().split(" ")]

        ob = Solution()
        print(ob.longestCommonPrefix(arr))

# } Driver Code Ends