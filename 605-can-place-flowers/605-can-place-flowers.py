class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
          if i == 0:
            if (len(flowerbed)==1 or flowerbed[i + 1] == 0) and flowerbed[i] == 0:
              n -= 1
              flowerbed[i] = 1
              if n == 0:
                return True
              pass
          if i == len(flowerbed) - 1:
            if flowerbed[i - 1] == 0 and flowerbed[i] == 0:
              n -= 1
              flowerbed[i] = 1
              if n == 0:
                return True
              pass
          if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
            n -= 1
            flowerbed[i] = 1
            
          if n == 0:
            return True
        if n <= 0:
          return True
        return False