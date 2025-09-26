class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        arr = []
        for i in range(len(s)):
            if s[i].isalnum():
                arr.append(s[i])

        s = ''.join(arr)

        i = 0
        j = len(s) - 1
        while i<=j:
            if s[i] != s[j]:
                return False
            i+=1
            j-=1
        return True