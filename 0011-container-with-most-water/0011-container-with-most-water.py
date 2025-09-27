class Solution:
    def maxArea(self, height: List[int]) -> int:
        #two pointer
        #start from the ends
        #move whichever pointer is lowest
        n = len(height)
        if n==2:
            return min(height)
        area = 0

        i = 0
        j = n - 1

        while i<j:
            curr_area = (j-i) * min(height[j],height[i])
            area = max(area, curr_area)
            if height[i] < height[j]:
                i+=1
            else:
                j-=1
        
        return area

