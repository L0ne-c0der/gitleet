class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 3:
            return sum(nums)
        nums.sort() #[-1, 2,1,-4]
        min_diff = 1001
        result = 0
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums) - 1
            while l<r and l<len(nums) and r>-1:
                temp_sum = nums[i] + nums[l] + nums[r]
                if abs(target - temp_sum) < min_diff:
                    min_diff = abs(target - temp_sum)
                    result = temp_sum

                else:
                    if temp_sum > target:
                        r-=1
                    else:
                        l+=1

        return result


