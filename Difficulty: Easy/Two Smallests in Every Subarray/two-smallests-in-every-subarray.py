class Solution:
    def pairWithMaxSum(self, arr):
        #code here
        ln = len(arr)
        if ln<2:
            return -1
        else:
            return max(num1+num2 for num1, num2 in zip(arr, arr[1:]))


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split("\n")

    t = int(data[0])
    lines = data[1:]

    for line in lines:
        s = list(map(int, line.strip().split()))
        solution = Solution()
        res = solution.pairWithMaxSum(s)
        print(res)

# } Driver Code Ends