class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sor_val = 0
        for x in nums:
            sor_val = sor_val ^ x
        return sor_val