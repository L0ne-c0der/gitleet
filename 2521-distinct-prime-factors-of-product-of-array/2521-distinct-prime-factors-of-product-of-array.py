class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def find_primes(n):

            factors = set()
            if n % 2 == 0:
                 factors.add(2)
                 while n % 2 == 0:
                    n /= 2
                
            for i in range(3, int(math.sqrt(n))+1, 2):
                if n % i == 0:
                    factors.add(i)
                    while n % i == 0:
                        n /= i
            if n > 2:
                factors.add(n)
            return factors

        distinct_factors = set()
        for i in nums:
            distinct_factors.update(find_primes(i))
        
        return len(distinct_factors)