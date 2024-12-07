class Solution:
    #User function Template for python3
    #Function to count inversions in the array.
    def inversionCount(self, arr):
        # Your Code Here
        def merge_and_count(arr, temp_arr, left, mid, right):
            i = left    # Starting index for the left subarray.
            j = mid + 1 # Starting index for the right subarray.
            k = left    # Starting index to be sorted.
            inv_count = 0
            
            # Conditions are checked to ensure that i doesn't exceed mid and j doesn't exceed right.
            while i <= mid and j <= right:
                if arr[i] <= arr[j]:
                    temp_arr[k] = arr[i]
                    i += 1
                else:
                    # There are mid - i inversions because all the remaining elements in the left subarray
                    # (arr[i], arr[i+1], ..., arr[mid]) are greater than arr[j].
                    temp_arr[k] = arr[j]
                    inv_count += (mid-i + 1)
                    j += 1
                k += 1

            # Copy the remaining elements of left subarray, if any.
            while i <= mid:
                temp_arr[k] = arr[i]
                i += 1
                k += 1

            # Copy the remaining elements of right subarray, if any.
            while j <= right:
                temp_arr[k] = arr[j]
                j += 1
                k += 1

            # Copy the sorted subarray into Original array.
            for i in range(left, right + 1):
                arr[i] = temp_arr[i]

            return inv_count

        # Function to implement merge sort and count inversions.
        def merge_sort_and_count(arr, temp_arr, left, right):
            inv_count = 0
            if left < right:
                # Mid of the array.
                mid = (left + right)//2
                inv_count += merge_sort_and_count(arr, temp_arr, left, mid)
                inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)
                inv_count += merge_and_count(arr, temp_arr, left, mid, right)

            return inv_count

        # Create a temporary array.
        temp_arr = [0]*len(arr)
        return merge_sort_and_count(arr, temp_arr, 0, len(arr) - 1)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a))
        print("~")

# } Driver Code Ends