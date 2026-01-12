from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we can try a dict of list
        #the key could be an ordered string or ordered tuple

        maps = defaultdict(list)
        for string in strs:
            str_tuple = tuple(sorted(string))
            maps[str_tuple].append(string)
            
        return list(maps.values())
        

            