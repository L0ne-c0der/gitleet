class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        set1 = set(nums)
        set2 = set([i for i in range(1,len(nums)+1)])
        final_set = set2 - set1
        return list(final_set)
        