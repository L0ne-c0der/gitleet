class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #we have to find the PREfix
        #so, all the words will be like pre-w1, pre-w2, pre-w3
        #if we sort the strings, we get it such that the smallest 
        #words will be in the first
        #and the largest will be in the last
        #so, if we find the common prefix of the largest and smallest
        #words, we get the common prefix of all the words
        #Note: sorting gives as [abcd, abd]

        strs.sort()
        small = strs[0]
        large = strs[-1]
        result = ""
        for i in range(min(len(small), len(large))):
            if not (small[i] == large[i]):
                break
            result+=small[i]
        return result
            
