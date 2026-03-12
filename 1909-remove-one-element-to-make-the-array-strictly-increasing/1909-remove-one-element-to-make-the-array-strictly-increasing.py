class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        '''
        We check for 2 drops.

        When there is a first drop, 
        we check if the number at 'pos+1' index 
        is greater than 'pos-1'

        1. If yes, then we drop the current number arr[pos], 
        like dropping 3 in 1,3,2

        2. If no, then we drop the next number, as it would be like [2, 3, 1], and hence we drop arr[pos+1], in this case, '1'

        Then, we check for another drop. 

        If 2 (or more) drops present, we will return False, else True
        '''
        if len(nums)<=2:
            return True
        count = 0
        i = 0
        while i < len(nums)-1 and count<2:
            if nums[i] >= nums[i+1]:  #if current >= next
                if i==0:
                    nums[i] = 0 # for cases where 2 pos = 0 pos
                    #like 2, 1, 2
                    
                elif i>0 and (nums[i+1] > nums[i-1]): #if prev < next
                    nums[i] = nums[i-1] #replace curr with prev 
                else:
                    nums[i+1] = nums[i] #replace next with curr
                count+=1 #increase count
            i+=1

        return False if count>=2 else True     
                
        


