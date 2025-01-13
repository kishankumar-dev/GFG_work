
class Solution:
    def maxWater(self, arr):
        # code here
        max_area = 0
        left = 0
        right = len(arr) - 1
        
        # Use two-pointer approach
        while left < right:
            # Calculate the area
            width = right - left
            height = min(arr[left], arr[right])
            current_area = width * height
            
            # Update the maximum area
            max_area = max(max_area, current_area)
            
            # Move the pointers
            if arr[left] < arr[right]:
                left += 1
            else:
                right -= 1
                
        return max_area

#{ 
 # Driver Code Starts
#Initial template for Python 3

import math


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.maxWater(arr))

        t -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends