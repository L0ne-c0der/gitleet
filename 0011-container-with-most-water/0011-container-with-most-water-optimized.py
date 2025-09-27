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

            min_h = min(height[j],height[i])
            curr_area = (j-i) * min_h
            area = max(area, curr_area)

            while i < j and height[i] <= min_h:
                i+=1
            while i < j and height[j] <= min_h:
                j-=1
        
        return area

