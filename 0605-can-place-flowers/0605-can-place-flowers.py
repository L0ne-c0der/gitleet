class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], k: int) -> bool:
        
        n = len(flowerbed)

        for i in range(n):
            prev = 0 if i==0 else flowerbed[i-1]
            next = 0 if i==(n-1) else flowerbed[i+1]
            if next==prev==flowerbed[i]==0:
                flowerbed[i] = 1
                k-=1
            if k==0:
                return True

        return k==0
