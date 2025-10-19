class Solution:
    def findDuplicate(self, nums):
        low, high = 1, len(nums) - 1  # Values range from 1 to n (n = len(nums)-1)
        
        while low < high:
            mid = (low + high) // 2
            count = 0
            
            # Count numbers ≤ mid
            for num in nums:
                if num <= mid:
                    count += 1
            
            # If count > mid, duplicate is in [low, mid]
            if count > mid:
                high = mid
            # Else, duplicate is in [mid+1, high]
            else:
                low = mid + 1
        
        return low