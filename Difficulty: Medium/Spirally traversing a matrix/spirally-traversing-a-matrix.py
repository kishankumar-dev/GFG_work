class Solution:
    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, mat):
        # code here
        n = len(matrix)
        m = len(matrix[0])
        up, left = 0, 0
        right, down = m - 1, n - 1
        ans = []
        while left <= right and up <= down:
            for i in range(left, right + 1):
                ans.append(matrix[up][i])
            up += 1
            for i in range(up, down + 1):
                ans.append(matrix[i][right])
            right -= 1
            if up <= down:
                for i in range(right, left - 1, -1):
                    ans.append(matrix[down][i])
                down -= 1
            if left <= right:
                for i in range(down, up - 1, -1):
                    ans.append(matrix[i][left])
                left += 1
        return ans

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1
    for _ in range(t):
        r = int(data[index])
        c = int(data[index + 1])
        index += 2
        matrix = []
        for i in range(r):
            row = list(map(int, data[index:index + c]))
            matrix.append(row)
            index += c

        solution = Solution()
        result = solution.spirallyTraverse(matrix)
        print(" ".join(map(str, result)))
        print("~")

# } Driver Code Ends