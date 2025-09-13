class Solution:
    def minCost(self, n, m, x, y):
        # code here
        x.sort(reverse=True)
        y.sort(reverse=True)

        # Initialize counters for segments
        horizontal_pieces = 1
        vertical_pieces = 1

        i = j = 0
        total_cost = 0

        # Greedily pick the higher cost cut
        while i < len(x) and j < len(y):
            if x[i] > y[j]:
                total_cost += x[i] * horizontal_pieces
                vertical_pieces += 1
                i += 1
            else:
                total_cost += y[j] * vertical_pieces
                horizontal_pieces += 1
                j += 1

        # Add remaining vertical cuts
        while i < len(x):
            total_cost += x[i] * horizontal_pieces
            i += 1

        # Add remaining horizontal cuts
        while j < len(y):
            total_cost += y[j] * vertical_pieces
            j += 1

        return total_cost
        
        
        
