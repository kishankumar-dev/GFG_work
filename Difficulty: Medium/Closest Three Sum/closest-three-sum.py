#User function Template for python3

# arr    : list of integers denoting the elements of the array
# target : as specified in the problem statement

class Solution:
    def threeSumClosest (self, arr, target):
    # Your Code Here
        arr.sort()
        min_diff, n = float('inf'), len(arr)
        
        for i in range(n-2):
            l, h = i+1, n-1
            
            while l < h:
                s = arr[i]+arr[l]+arr[h]
                diff = abs(s-target)
                
                if diff<min_diff:
                    min_diff=diff
                    closest_s=s
                elif diff == min_diff:
                    closest_s = max(s, closest_s)
                
                
                if s>target:
                    h-=1
                else:
                    l+=1
 
        return closest_s


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        A = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.threeSumClosest(A, k))

# } Driver Code Ends