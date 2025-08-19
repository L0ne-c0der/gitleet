class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for digit in digits:
            num = num*10 + digit
        num +=1
        result = []
        while num>0:
            digit = (num % 10)
            result.append(digit)
            num = num//10
        return result[::-1]
            
        
