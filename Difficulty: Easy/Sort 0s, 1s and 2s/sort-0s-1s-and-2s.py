#{ 
 # Driver Code Starts

# } Driver Code Ends
class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        # code here
        count0=0
        count1=0
        count2=0
        l=len(arr)
        for i in range(l):
            if arr[i]==0:
                count0+=1
            elif arr[i]==1:
                count1+=1
            else:
                count2+=1
        arr[:]=[0]*count0 + [1]*count1 + [2]*count2
        return arr

#{ 
 # Driver Code Starts.
def main():
    t = int(input().strip())  # Read the number of test cases
    ob = Solution()

    while t > 0:
        t -= 1
        arr = list(map(int,
                       input().strip().split())
                   )  # Read the array as space-separated integers
        ob.sort012(arr)  # Sort the array

        print(' '.join(map(str, arr)))  # Print the sorted array
        print("~")
        
if __name__ == "__main__":
    main()

# } Driver Code Ends