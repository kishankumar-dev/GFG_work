class Solution:
    def sort012(self, arr):
        # code here
        ze=0
        on=0
        tw=0

        o=False
        t=False
        l=len(arr)
        for i in arr:
            if i==0:
                arr[ze]=0
                ze+=1
                if o:
                    arr[on]=1
                on+=1
                if t:
                    arr[tw]=2
                tw+=1
            elif i==1:
                o=True
                arr[on]=1
                on+=1
                if t:
                    arr[tw]=2
                tw+=1
            else:
                t=True
                arr[tw]=2
                tw+=1
                
        return arr