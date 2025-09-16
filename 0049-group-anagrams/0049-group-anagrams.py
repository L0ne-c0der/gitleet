class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create a list of dictionaries
        #if the dictionary already present, no need
        #else, we will add the dict, and then something

        dict_list = []
        res = []
        for string in strs:
            mapp = dict()
            for char in string:
                mapp[char] = mapp.get(char,0) + 1
             
            if mapp not in dict_list:
                dict_list.append(mapp)
                res.append([string])

            else:
                idx = dict_list.index(mapp)
                res[idx].append(string)
        
        return res


                

