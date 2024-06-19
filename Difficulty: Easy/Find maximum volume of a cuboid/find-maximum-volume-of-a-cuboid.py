#User function Template for python3

class Solution:
    def maxVolume(self, perimeter, area):
        #code here
        length=(perimeter-math.sqrt(perimeter*perimeter-24*area))/12#length of the cuboid
        height=(perimeter/4)-2*length #height of the cuboid
        volume=length*length*height #Volume of the cuboid
        return round(volume,2)

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import math
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        perimeter, area = [int(x) for x in input().split()]

        ob = Solution()
        print('%.2f' % ob.maxVolume(perimeter, area))

# } Driver Code Ends