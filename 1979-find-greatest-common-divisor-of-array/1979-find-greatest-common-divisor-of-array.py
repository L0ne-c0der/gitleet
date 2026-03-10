class Solution:
    def findGCD(self, nums: List[int]) -> int:
        small = min(nums)
        large = max(nums)

        def gcd(a , b):
            if a%b ==0:
                return b
            
            if b > a:
                a, b = b, a

            while b!=0:
                a,b = b, a%b
            
            return a
        
        return gcd(small, large)