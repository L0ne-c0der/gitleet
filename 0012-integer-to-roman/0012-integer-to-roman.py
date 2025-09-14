class Solution:
    def intToRoman(self, num: int) -> str:
        romans = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
        nums = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        temp = num
        result = ""
        for i in range(len(nums)-1, -1, -1):
            while temp >= nums[i]:
                temp -= nums[i]
                result += romans[i]

        return result


