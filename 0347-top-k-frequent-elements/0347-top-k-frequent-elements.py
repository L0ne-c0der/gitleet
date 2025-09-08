class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapp = dict()
        res = []
        for num in nums:
            if num in mapp:
                mapp[num] = mapp[num] + 1
            else:
                mapp[num] = 1

        counts = list(mapp.values())
        counts.sort(reverse=True)
        counts = counts[:k]
        
        for key, value in mapp.items():
            if value in counts:
                res.append(key)

        return res
        
