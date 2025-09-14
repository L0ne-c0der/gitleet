class Solution:
    def find132pattern(self, nums: List[int]) -> bool:

    #using stack (more like monotonic stack)
    #we keep track of the most min value before each index j in "min" array
    #then we iterate the nums array in reverse
    #if nums[j] > min_array[j] ,i.e, if arr[j] > arr[i]:
    #check if stack[top] < min[j]: pop, so that we get arr[k](stack) > arr[i](min)
    # then, check if stack top is less than nums[j], so arr[k] < arr[j] 
    #  if so then return True, else append nums[j] to stack
        if len(nums) < 3:
            return False
        stack = []
        min_array = [-1] * len(nums)
        min_array[0] = nums[0]
        for i in range(1, len(nums)):
            min_array[i] = min(min_array[i - 1], nums[i])

        for j in range(len(nums) - 1, -1, -1):
            if nums[j] <= min_array[j]:
                continue
            while stack and stack[-1] <= min_array[j]:
                stack.pop()
            if stack and stack[-1] < nums[j]:
                return True
            stack.append(nums[j])
        return False