class Solution:
    def findMoves(self, chairs, passengers):
        # code here
        chairs.sort()
        passengers.sort()
        moves = 0
        for c,p in zip(chairs, passengers):
            moves += abs(c -p)
        return moves