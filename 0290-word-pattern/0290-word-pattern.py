class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
#we will use the zip function here

#zip function maps one item in one ele, with one item (of same index) in another ele, and add it to to a tuple

#ex: list(zip([1,2,3], 'abc')) o/p: [(1,'a'),(2,'b),(3,'c')]

        s_list = s.split()
        return len(set(zip(pattern, s_list))) == len(set(s_list)) == len(set(pattern)) and len(pattern) == len(s_list)