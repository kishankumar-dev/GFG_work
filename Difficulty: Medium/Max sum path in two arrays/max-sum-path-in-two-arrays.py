#Your task is to complete this function
#Function should return an integer denoting the required answer
class Solution:
    def maxPathSum(self, arr1, arr2):
        # Code here
        sum1, sum2, max_sum = 0, 0, 0
        m, n = len(arr1), len(arr2)
        i, j = 0, 0
        while i < m and j < n:
            if arr1[i] < arr2[j]:
                sum1 += arr1[i]
                i += 1
            elif arr1[i] == arr2[j]:
                max_sum += max(sum1, sum2) + arr1[i]
                i += 1
                j += 1
                sum1 = sum2 = 0
            else:
                sum2 += arr2[j]
                j += 1
        sum1 += sum(arr1[i:])
        sum2 += sum(arr2[j:])
        max_sum += max(sum1, sum2)
        return max_sum

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxPathSum(arr1, arr2)
        print(ans)

# } Driver Code Ends