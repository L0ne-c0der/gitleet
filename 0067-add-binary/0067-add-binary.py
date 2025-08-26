class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_len = len(a)
        b_len = len(b)

        # Pad with leading zeros
        if a_len < b_len:
            a = ('0' * (b_len - a_len)) + a
        else:
            b = ('0' * (a_len - b_len)) + b

        carry = 0
        output = ''
        for i in range(len(a)-1, -1, -1):
            dig_sum = int(a[i]) + int(b[i]) + carry
            output = str(dig_sum % 2) + output
            carry = dig_sum // 2

        if carry:
            output = '1' + output
        return output
