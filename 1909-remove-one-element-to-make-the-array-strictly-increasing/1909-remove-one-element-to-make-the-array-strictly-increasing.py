class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        def is_sorted(arr) -> bool: 
            ''' To check if the given array is increasing or not.'''
            l = len(arr)
            if l == 1:
                return True    
            for i in range(l-1):
                if arr[i] >= arr[i+1]:
                    return False
            return True

        #even in case the array is already in increasing order, 
        #removing first element will still keep it the same

        for i in range(len(nums)):
            if is_sorted(nums[:i] + nums[i+1:]): 
                # if array is increasing after removing 
                #element in index i
                return True

        # even with all combination of elements 
        #being removed, it is unsorted
        return False
