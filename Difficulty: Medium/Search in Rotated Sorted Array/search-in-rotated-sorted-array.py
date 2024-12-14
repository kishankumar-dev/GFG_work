#User function Template for python3

class Solution:
    def search(self,arr,key):
        # Complete this function
        s = 0
        e = len(arr) - 1
        
        while s <= e:
            m = s + (e - s) // 2
            
            if arr[m] == key:
                return m
            
            if arr[s] <= arr[m]:
                if arr[s] <= key < arr[m]:
                    e = m - 1
                else:
                    s = m + 1
            else:
                if arr[m] < key <= arr[e]:
                    s = m + 1
                else:
                    e = m - 1
        
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        A = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.search(A, k))
        print("~")

# } Driver Code Ends