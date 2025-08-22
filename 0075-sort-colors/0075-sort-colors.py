class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = [0]*3
        for i in range(len(nums)):
            counter[nums[i]] += 1
        
        j = 0
        for i in range(3):
            while counter[i]!=0:
                nums[j] = i
                counter[i] = counter[i] - 1
                j+=1
        