class Solution:
    def isHappy(self, n: int) -> bool:
        prev = []
        def _isHappy(n , prev):
            if n==1:
                return True
            if n in prev:
                return False
            
            prev.append(n)
            sum = 0
            while n>0:
                digit = n%10
                sum += digit*digit
                n = n // 10
            return _isHappy(sum, prev)

        return _isHappy(n, prev)