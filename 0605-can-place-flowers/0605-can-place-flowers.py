class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        flowerbed = [0] + flowerbed + [0]

        if n==0:
            return True

        k = len(flowerbed)

        for i in range(1, k-1):
            prev = flowerbed[i-1]
            next = flowerbed[i+1]
            if next==prev==flowerbed[i]==0:
                flowerbed[i] = 1
                n-=1
            if n==0:
                return True

        return n==0
