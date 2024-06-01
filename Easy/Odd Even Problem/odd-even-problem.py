
class Solution:
    def oddEven(self, s : str) -> str:
        # code here
        ans = 0
        d = {}
        
        #count frequency of all charactors
        for i in s:
            if i not in d:
                d.update({i:1})
            else:
                d[i]+=1
                
        for i in d:
            #check if frequencey is odd and position is odd
            #ascii values of lower charactor itself indicates it is in even or odd position
            if d[i]%2==1 and (ord(i))%2==1:
                ans+=1
                
            #check if frequencey is even and position is even
            elif d[i]%2==0 and (ord(i))%2==0:
                ans+=1
        return 'EVEN' if ans%2==0 else 'ODD'
        



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        s = (input())

        obj = Solution()
        res = obj.oddEven(s)

        print(res)

# } Driver Code Ends