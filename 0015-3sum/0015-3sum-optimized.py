class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if i>0 and nums[i]==nums[i-1]:
                continue
                
            target = nums[i] * (-1)
            l = i+1
            r = len(nums) - 1
            while l<r:
                value = nums[l] + nums[r]
                if  value == target:
                    result.append([nums[i],nums[l], nums[r]]) 
                    l+=1
                    while nums[l] == nums[l -  1] and l<r :
                        l+=1
            
                elif value > target:
                    r-=1
                else:
                    l+=1
        
        return result


