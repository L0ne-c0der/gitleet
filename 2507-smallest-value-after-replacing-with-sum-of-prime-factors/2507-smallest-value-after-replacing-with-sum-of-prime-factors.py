class Solution:
    def smallestValue(self, n: int) -> int:
    #    def prime_factors(n):
        prev = n
        ans = 0
        while n % 2 == 0:            
            ans += 2
            n //= 2
        
        for i in range(3, n+1, 2):
            while n % i == 0:
                ans += i
                n //= i
        
        return self.smallestValue(ans) if ans != prev else ans



        

        
