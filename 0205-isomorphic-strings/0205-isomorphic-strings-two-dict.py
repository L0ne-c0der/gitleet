class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        mapp_t = dict()
        mapp_s = dict()
        for i in range(len(s)):
            if s[i] in mapp_t and mapp_t[s[i]]!=t[i]:
                return False
            elif t[i] in mapp_s and mapp_s[t[i]]!=s[i]:
                return False
            mapp_t[s[i]] = t[i]
            mapp_s[t[i]] = s[i]

        return True