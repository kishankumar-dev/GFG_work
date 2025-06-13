#User function Template for python3

class Solution:
    def kokoEat(self,arr,k):
        # Code here        
        def calculate_hours_taken(s_speed):
            total_hours = 0
            for pile_size in arr:
                total_hours += (pile_size + s_speed - 1) // s_speed
            return total_hours

        low = 1
        high = max(arr)
        ans = high

        while low <= high:
            mid = (low + high) // 2
            hours = calculate_hours_taken(mid)

            if hours <= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans