#User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        # code here
        d={0:-1}
        pre=0
        for c,i in enumerate(arr):
            pre+=i
            if (pre-target) in d:
                return [d[pre-target]+2,c+1]
            d[pre]=c
        return [-1]

#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        d = int(input().strip())
        ob = Solution()
        result = ob.subarraySum(arr, d)
        print(" ".join(map(str, result)))
        tc -= 1
        print("~")

# } Driver Code Ends