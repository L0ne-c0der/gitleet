class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #idea is to store the data with modification in another array
        #then we move the data back to the given array

        n = len(nums)
        k = k % n #so that if k > n, we will know the min no of rotations
        
        rotated = [0] * n #temp array

        for i in range(n):
            new_pos = (i+k)%n
            rotated[new_pos] = nums[i] 
            #take example last index, say 5. Then if k =3 then it will be 
            #5+3 = 8, so 8%5 = 3, where it will be placed
        
        #now to move this rotated values to given array
        for i in range(n):
            nums[i] = rotated[i]
