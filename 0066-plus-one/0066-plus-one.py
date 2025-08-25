class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = True
        for i in range(len(digits)-1,-1,-1):
            if carry:
                digits[i] = digits[i] + 1
            if digits[i] == 10:
                carry = True
                digits[i] = digits[i] % 10
            else:
                carry = False
        if carry:
            return [1] + digits
        return digits

            
        
