class Solution:
    def findAndPlace(self, arr, idx):
        val = idx + 1
        target_idx = arr.index(val)
        arr[idx], arr[target_idx] = arr[target_idx], arr[idx]

    def checkSorted(self, arr):
        misplaced = 0
        for idx, val in enumerate(arr):
            if val != idx + 1:
                misplaced += 1
                self.findAndPlace(arr, idx)
            if misplaced > 2:
                return False
        
        if misplaced in (0, 2):
            return True
        return False
                

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        arr = list(map(int, input().split()))

        sol = Solution()
        result = sol.checkSorted(arr)
        if result:
            print("true")
        else:
            print("false")

# } Driver Code Ends