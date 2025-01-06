#User function Template for python3
class Solution:
    def sumClosest(self, arr, target):
        # code here
        if len(arr) < 2:
            return []
        
        # Sort the array
        arr.sort()
        left, right = 0, len(arr) - 1
        closest_sum = float('inf')
        result = []
        
        while left < right:
            current_sum = arr[left] + arr[right]
            abs_diff = abs(current_sum - target)
            max_abs_diff = abs(arr[right] - arr[left])
            
            # Update the result if a closer sum is found
            if abs_diff < abs(closest_sum - target) or (
                abs_diff == abs(closest_sum - target) and 
                (not result or max_abs_diff > abs(result[1] - result[0]))
            ):
                closest_sum = current_sum
                result = [arr[left], arr[right]]
            
            # Move pointers based on the current sum
            if current_sum < target:
                left += 1
            else:
                right -= 1
        
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())
    while t > 0:
        arr = list(map(int, input().strip().split()))
        target = int(input().strip())
        ob = Solution()
        ans = ob.sumClosest(arr, target)
        if not ans:
            print("[]")
        else:
            print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends