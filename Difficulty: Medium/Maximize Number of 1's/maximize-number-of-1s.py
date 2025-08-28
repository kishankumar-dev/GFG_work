class Solution:
    def maxOnes(self, arr, k):
        # code here
        zeros = 0
        left = 0
        maxlen = 0

        for right in range(len(arr)):
            if arr[right]==0:
                zeros+=1
                while(zeros>k):
                    if arr[left]==0:
                        zeros-=1
                    left+=1
                    
            maxlen = max(maxlen,right-left+1)
            
        return maxlen