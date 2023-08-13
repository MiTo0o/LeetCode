class Solution:
    def isHappy(self, n: int) -> bool:
        sat = set()
        while n not in sat:
          sat.add(n)
          n = sum(int(i) ** 2 for i in str(n))

        return n == 1