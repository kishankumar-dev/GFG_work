#User function Template for python3
class Solution:

	def matchPairs(self, n, nuts, bolts):
		# code here
		order = ["!", "#", "$", "%", "&", "*", "?", "@", "^"]
    
        nut_set = set(nuts)
        bolt_set = set(bolts)
        
        sorted_nuts = []
        sorted_bolts = []
        
        for char in order:
            if char in nut_set and char in bolt_set:
                sorted_nuts.append(char)
                sorted_bolts.append(char)
        nuts[:] = sorted_nuts
        bolts[:] = sorted_bolts

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        nuts = list(map(str, input().strip().split()))
        bolts = list(map(str, input().strip().split()))
        ob = Solution()
        ob.matchPairs(n, nuts, bolts)
        for x in nuts:
            print(x, end=" ")
        print()
        for x in bolts:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends