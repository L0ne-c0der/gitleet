class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
       length = len(needle)
       if length > len(haystack):
        return -1
       
       if needle == haystack:
        return 0

       for i in range(len(haystack)):
         if haystack[i:i+length] == needle:
            return i
       return -1



        