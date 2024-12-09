#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def insertInterval(self, iv, ni):
        # Code here        
        a, i = [], 0

        while i < len(iv) and iv[i][1] < ni[0]: 
            a.append(iv[i])
            i += 1

        while i < len(iv) and iv[i][0] <= ni[1]: 
            ni = [min(ni[0], iv[i][0]), max(ni[1], iv[i][1])]
            i += 1

        a.append(ni)
        a.extend(iv[i:])
        
        return a

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        intervals = [list(map(int, input().split())) for i in range(N)]
        newEvent = list(map(int, input().split()))
        ob = Solution()
        res = ob.insertInterval(intervals, newEvent)
        print('[', end = '')
        for i in range(len(res)):
            print('[', end = '')
            print(str(res[i][0])+','+str(res[i][1]), end = '')
            print(']', end = '')
            if i < len(res)-1:
                print(',', end='')
        print(']')
        print("~")
# } Driver Code Ends