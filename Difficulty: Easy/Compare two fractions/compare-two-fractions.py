#User function Template for python3


class Solution:
    def compareFrac (self, str):
        # code here
        str1=str.split(',')
        final1=str1[0]
        final2=str1[1]
        for i in range(len(str1)):
            str1[i]=str1[i].split('/')
        a=str1[0][0]
        b=str1[0][1]
        a=int(a)
        b=int(b)
        div1=a/b
        a1=str1[1][0]
        b1=str1[1][1]
        a1=int(a1)
        b1=int(b1)
        div2=a1/b1
        if div1>div2:
            return final1.strip()
        elif div1<div2:
            return final2.strip()
        else:
            return 'equal'



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import re

if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        str = input()
        print(ob.compareFrac(str))

# } Driver Code Ends