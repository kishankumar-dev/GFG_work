
class Solution:
    def decodedString(self, s):
        # code here
        n = len(s)
        stopper = "-1"
        def parse(s, i):
            r = ""
            while i < n:
                p, i = parse_item(s, i)
                if p == stopper:
                    break
                r += p
            return r, i
        def parse_item(s, i):
            if i >= n:
                return "", n
            if s[i] == '[':
                return parse(s, i+1)
            if s[i] == ']':
                return stopper, i+1
            if not s[i].isdigit():
                return s[i], i+1
            e = 0
            while s[i].isdigit():
                e = e*10 + ord(s[i]) - ord('0')
                i += 1
            r, i = parse_item(s, i)
            return r*e, i
        
        r, _ = parse(s, 0)
        return r

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()

        ob = Solution()
        print(ob.decodedString(s))
        print("~")

# } Driver Code Ends