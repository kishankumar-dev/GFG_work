class Solution:
    def catchThieves(self, arr, k):
        #code here
        if arr.count("P") == 0 or arr.count("T")== 0:
            return 0
        police = []
        thief = []
    
        for i in range(len(arr)):
            if arr[i] == 'P':
                police.append(i)
            else:
                thief.append(i)
        
        i = j = 0
        caught = 0
        
        while i < len(police) and j < len(thief):
            if abs(police[i] - thief[j]) <= k:
                caught += 1
                i += 1
                j += 1
            elif police[i] < thief[j]:
                i += 1
            else:
                j += 1
        
        return caught

