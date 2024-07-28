#User function Template for python3
class Solution:
	def removeDups(self, str):
		# code here
		result = ''
		space = [0]*26
		for each in str:
		    index = ord(each)-ord('a')
		    if space[index]==0:
		        result+=each
		        space[index]=1
		return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.removeDups(s)

        print(answer)

# } Driver Code Ends