class Solution:
    def countPrimes(self, n: int) -> int:
        if n<2:
            return 0
        
        sieve = [True] * (n)
        sieve[0] = False
        sieve[1] = False
        i=2
        while i*i<n:
            if sieve[i]:
                for j in range(i + i, n, i):
                    sieve[j] = False
            i +=1
        count = 0
        for val in sieve:
            if val:
                count+=1
        return count