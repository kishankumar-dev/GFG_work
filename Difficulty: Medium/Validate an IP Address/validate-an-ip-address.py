#User function Template for python3
class Solution:
    def isValid(self, str):
        #code here
        a = str.split(".")
        b = []
        t = "true"
        f = "false"
        if len(a)==4:
            for i in a:
                a = i
                a = int(a)
                b.append(a)
            if (b[0]<=255 and b[1]<=255) and (b[2]<=255 and b[3]<=255):
                return t
        else:
            return f



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        ob = Solution()
        if (ob.isValid(s)):
            print("true")
        else:
            print("false")

# } Driver Code Ends