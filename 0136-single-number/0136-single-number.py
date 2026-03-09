class Solution:
    def singleNumber(self, arr: List[int]) -> int:
        if len(arr) < 2:
            return arr[0]

        res = arr[0]
        for i in range(1, len(arr)):
            res = res ^ arr[i]
        return res