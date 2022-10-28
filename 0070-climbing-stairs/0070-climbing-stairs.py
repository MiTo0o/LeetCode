class Solution:
    def climbStairs(self, n: int) -> int:
        x, d = 0, 1
        for i in range(n):
            x, d = d, x + d
        return d