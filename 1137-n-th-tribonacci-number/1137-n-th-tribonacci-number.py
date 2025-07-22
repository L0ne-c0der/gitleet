class Solution:
    def tribonacci(self, n: int) -> int:
        if n<=1:
            return n
        if n==2:
            return 1
        memory_arr = [-1] * (n+1)
        memory_arr[0] = 0
        memory_arr[1] = memory_arr[2] = 1
        for i in range(3,n+1):
            memory_arr[i] = memory_arr[i-1] + memory_arr[i-2] + memory_arr[i-3]
        return memory_arr[n]