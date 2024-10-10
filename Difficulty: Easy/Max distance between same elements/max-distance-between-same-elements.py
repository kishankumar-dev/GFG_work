class Solution:
    # Your task is to Complete this function
    # functtion should return an integer
    def maxDistance(self, arr):
        # Code here
        tracker = {}
        max_distance = 0
        for i in range(0, len(arr)):
            element = arr[i]
            if element not in tracker:
                tracker[element] = [i, i]
            else:
                tracker[element][1] = i
                distance = tracker[element][1] - tracker[element][0]
                if distance > max_distance: max_distance = distance
        return max_distance


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.maxDistance(arr))

# } Driver Code Ends