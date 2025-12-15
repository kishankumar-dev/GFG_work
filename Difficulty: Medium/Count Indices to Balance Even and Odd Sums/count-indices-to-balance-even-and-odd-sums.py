class Solution:
    def cntWays(self, arr):
        # code here
        total_even = sum(arr[i] for i in range(0, len(arr), 2))
        total_odd = sum(arr[i] for i in range(1, len(arr), 2))
    
        left_even = left_odd = 0
        count = 0
    
        for i, val in enumerate(arr):
            if i % 2 == 0:
                right_even = total_even - left_even - val
                right_odd = total_odd - left_odd
            else:
                right_even = total_even - left_even
                right_odd = total_odd - left_odd - val
    
            if left_even + right_odd == left_odd + right_even:
                count += 1
    
            if i % 2 == 0:
                left_even += val
            else:
                left_odd += val
    
        return count