class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True
        if len(flowerbed) == 1:
            return flowerbed[0] == 0
        for i in range(len(flowerbed)):
            if n == 0:
                return True
            if flowerbed[i] == 1:
                continue
            else:
                if i == 0:
                    if i+1 < len(flowerbed) and flowerbed[i+1] == 0 and n != 0:
                        flowerbed[i] = 1
                        n -= 1
                        continue
                if i == len(flowerbed)-1:
                    if i-1 >= 0 and flowerbed[i-1] == 0 and n != 0:
                        flowerbed[i] = 1
                        n -= 1
                        continue
                if i-1 >= 0 and i+1 < len(flowerbed) and flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and n != 0:
                    flowerbed[i] = 1
                    n -= 1
                    continue
        return n == 0