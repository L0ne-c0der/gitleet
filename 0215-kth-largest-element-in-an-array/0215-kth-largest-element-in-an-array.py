from heapq import heapify, heappop, heappush
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        
        return nums[0]