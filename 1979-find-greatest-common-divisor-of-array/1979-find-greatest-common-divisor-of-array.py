class Solution:
    def findGCD(self, nums: List[int]) -> int:
        small = min(nums)
        large = max(nums)

        def gcd(a , b):

            while b!=0:
                a,b = b, a%b
            
            return a
        
        return gcd(small, large)