
from typing import List


class Solution:
    def pairsum(self, arr : List[int]) -> int:
        # code here
        n = len(arr)
        m1,m2 = 0,0
        for i in range(n):
            if arr[i] >= m1:
                m2 = m1
                m1 = arr[i]
            elif arr[i] >= m2 and arr[i] < m1:
                m2 = arr[i]
        return m1 + m2



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        arr = list(map(int, input().strip().split()))

        obj = Solution()
        res = obj.pairsum(arr)

        print(res)

# } Driver Code Ends