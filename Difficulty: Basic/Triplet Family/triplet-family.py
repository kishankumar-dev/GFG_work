class Solution:
    def findTriplet(self, arr):
        length = len(arr)
        if length < 3:
            return False
        for i in range(length):
            for j in range(i + 1, length):
                if arr[i] + arr[j] in arr:
                    return True
        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3
# Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.findTriplet(arr)
        if (res):
            print("true")
        else:
            print("false")
        # print(res)
        print("~")
        t -= 1

# } Driver Code Ends