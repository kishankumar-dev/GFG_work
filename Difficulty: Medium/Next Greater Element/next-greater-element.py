# User function Template for python3

class Solution:
    # Function to find the next greater element for each element of the array.
    def nextLargerElement(self, arr):
        # code here
        ret=[]
        stk=[]
        for ix in range(len(arr)-1,-1,-1):
            ve=arr[ix]
            while stk and stk[-1]<=ve:
                stk.pop()
            ret.append(stk[-1] if stk else -1)
            stk.append(ve)
        return ret[::-1]

#{ 
 # Driver Code Starts
# Initial Template for Python 3

t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().nextLargerElement(arr)  # find the next greater elements

    # Output formatting
    if s:
        print(" ".join(map(str, s)))  # Print next greater elements
    else:
        print("[]")  # Print empty list if no next greater element is found
    print("~")
# } Driver Code Ends