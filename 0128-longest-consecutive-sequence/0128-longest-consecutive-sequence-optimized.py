class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        arr = list(set(nums))
        arr.sort()
        sizes = []
        size = 1
        longest = 1

        for i in range(1,len(arr)):
            if arr[i] != arr[i-1]+1:
                i+=1
                longest = max(size, longest)
                size = 1

            else:
                size+=1

        return max(longest, size)