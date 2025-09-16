class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def str_to_dict(string) -> dict:
            mapp = dict()
            for char in string:
                if char in mapp:
                    mapp[char] += 1
                    continue
                mapp[char] = 1
            return mapp
    
        return str_to_dict(s) == str_to_dict(t)