#User function Template for python3

#Complete this function
#Function to find maximum circular subarray sum.
def circularSubarraySum(arr):
    ##Your code here
    def kadane(arr):
        curr=0
        ans=arr[0]
        for i in arr:
            curr+=i
            ans=max(curr,ans)
            curr=max(curr,0)
        return ans
    max_sub_array=kadane(arr)
    total_sum=sum(arr)
    inverted_sum=kadane([-i for i in arr])
    max_circular_subarray_sum=total_sum+inverted_sum
    return max(max_sub_array,max_circular_subarray_sum)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
import sys

if __name__ == "__main__":
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        print(circularSubarraySum(arr))

        T -= 1

# } Driver Code Ends