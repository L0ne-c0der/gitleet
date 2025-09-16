from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #create a dictionary whose key is sorted value, and each key stores
        #list of string that have the same ordered characters
        #defaultdict is sub-class of dict()
        #initializes the dict with default values for a key 
        #based on parameter (default_factory) passed
        #if parameter is "int": default value for every key would be 0
        #else list: default value for every key would be []
        #else set: def val is {}

        mapp = defaultdict(list)

        for string in strs:
            key = "".join(sorted(string))
            mapp[key].append(string)
        
        return list(mapp.values())


                

