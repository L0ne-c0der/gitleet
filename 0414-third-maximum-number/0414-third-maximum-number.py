class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if not nums:
            return
        num_set = set(nums)
        unique_list = list(num_set)
        unique_list.sort(reverse=True)        
        if(len(unique_list)>=3):
            return unique_list[2]
        else:
            return unique_list[0]