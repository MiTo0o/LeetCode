class Solution:
    def climbStairs(self, n: int) -> int:
        x, d = 0, 1
        for i in range(n):
            temp = x + d
            x = d 
            d = temp
        return d
        print(d)