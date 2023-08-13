class Solution:
    def isHappy(self, n: int) -> bool:
        sat = set()
        while n not in sat:
          sat.add(n)
          n = self.sumSquare(n)

        return n == 1
      
    def sumSquare(self, n: int):
      s = 0
      while (n != 0):
          s += (n % 10) ** 2
          n = n // 10
      return s