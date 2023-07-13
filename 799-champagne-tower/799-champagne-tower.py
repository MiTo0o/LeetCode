class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
      dp = []
      for i in range(1, query_row + 3):
        dp.append([0] * i)
      dp[0][0] = poured
      for row in range(len(dp) - 1):
        for cup in range(len(dp[row])):
          if dp[row][cup] > 1:
            split = (dp[row][cup] - 1) / 2
            dp[row][cup] = 1
            # print('row', row, cup, len(dp))
            dp[row + 1][cup] += split
            dp[row + 1][cup + 1] += split
      
      
      
      for i in dp:
        print(i)
      return dp[query_row][query_glass]