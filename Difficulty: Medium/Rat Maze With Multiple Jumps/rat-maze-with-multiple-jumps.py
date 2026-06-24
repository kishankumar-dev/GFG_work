class Solution:
	def helper(self, x, y):
		if not self.valid(x, y):
            return False

        if self.dp[x][y] == False:
            return False

        self.ans[x][y] = 1

        if (x, y) == (self.row - 1, self.col - 1):
            return True

        for jump in range(1, self.matrix[x][y] + 1):
            if self.helper(x, y + jump) or self.helper(x + jump, y):
                return True

        self.ans[x][y] = 0
        self.dp[x][y] = False
        return False

    def shortestDist(self, matrix):
        self.matrix = matrix
        self.row = len(matrix)
        self.col = len(matrix[0])

        self.ans = [[0] * self.col for _ in range(self.row)]
        self.dp = [[None] * self.col for _ in range(self.row)]

        self.valid = lambda x, y: (
            (x, y) == (self.row - 1, self.col - 1)
            or (0 <= x < self.row and 0 <= y < self.col and matrix[x][y] > 0)
        )

        if self.helper(0, 0):
            return self.ans

        return [[-1]]

