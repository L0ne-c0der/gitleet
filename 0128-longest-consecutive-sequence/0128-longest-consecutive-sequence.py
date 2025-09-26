class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        arr = list(set(nums))
        arr.sort()
        sizes = []
        size = 1
        for i in range(1,len(arr)):
            if arr[i] != arr[i-1]+1:
                sizes.append(size)
                i+=1
                size = 1
            else:
                size+=1

        sizes.append(size)
            

        sizes.sort(reverse=True)
        return sizes[0]