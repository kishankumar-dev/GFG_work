#User function Template for python3
class Solution:
    def kPangram(self,string, k):
    # code here
        s=""
        for i in string:
            if i.isalpha():
                s+=i
        string=s
        if len(string)<26:
            return False
        d={}
        u=0
        for i in string:
            if i not in d.keys():
                u+=1
                d[i]=1
        if 26-u>k:
            return False
        else:
            return True

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        string = input()
        K = int(input())
        ob = Solution()
        a = ob.kPangram(string, K)
        if a:
            print("true")
        else:
            print("false")

# } Driver Code Ends