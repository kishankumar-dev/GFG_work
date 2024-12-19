
class Solution:
    def kthMissing(self, arr, k):
        # code here
        if arr[0] > k: 
            return k
        else:
            num = arr[0] 
            k = k - (arr[0] - 1)
        for ele in arr:
            if num < ele: 
                if k <= (ele - num):
                    return num + k - 1 
                else:
                    k = k - (ele - num) 
            num = ele + 1 
        return num + k -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.kthMissing(A, D)
        print(ans)
        print("~")

# } Driver Code Ends