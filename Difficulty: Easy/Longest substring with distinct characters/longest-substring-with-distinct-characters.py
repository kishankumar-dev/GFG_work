#User function Template for python3

class Solution:
    def longestUniqueSubstr(self, s):
        # code here
        freq_map = {}
        max_len, l = 1, 0
        for i in range(len(s)):
            freq_map[s[i]] = freq_map.get(s[i], 0) + 1
            while(freq_map[s[i]] > 1):
                freq_map[s[l]] -= 1
                l += 1
            max_len = max(max_len, i - l + 1)
        return max_len

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        ans = solObj.longestUniqueSubstr(s)

        print(ans)

        print("~")
# } Driver Code Ends