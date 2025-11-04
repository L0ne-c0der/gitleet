class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #using 2 pointer??
        #to check if they 2 strings are a permutation of another:
        #best to sort them and see if they are equal

        if len(s1) > len(s2):
            return False
        
        if s1 == s2:
            return True

        sorted_s1 = sorted(s1)
        length = len(s1)
        i = 0
        j = length
        while j<len(s2) + 1:
            if sorted_s1 == sorted(s2[i:j]):
                return True
            i+=1
            j+=1
        
        return False
        