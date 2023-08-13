class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
      flat = []
      index = 0
      for i in range(len(board)):
        for j in range(len(board[i])):
          flat.append(board[i][j])
          
      for i in range(0,len(flat),9):
        s = set(flat[i:i+9])
        s.discard('.')
        if sum(1 for j in flat[i:i+9] if j != '.') != len(s):
          return False
        
      for i in range(9):
        s = set(flat[i::9])
        s.discard('.')
        if sum(1 for j in flat[i::9] if j != '.') != len(s):
          return False
        
      start = 0
      for i in range(3):
        temp = [*flat[start:start+3],*flat[start+9:start+12],*flat[start+18:start+21]]
        s = set(temp)
        s.discard('.')
        if sum(1 for j in temp if j != '.') != len(s):
          return False
        start += 3
        
      start = 27
      for i in range(3):
        temp = [*flat[start:start+3],*flat[start+9:start+12],*flat[start+18:start+21]]
        s = set(temp)
        s.discard('.')
        if sum(1 for j in temp if j != '.') != len(s):
          return False
        start += 3
      
      start = 54
      for i in range(3):
        temp = [*flat[start:start+3],*flat[start+9:start+12],*flat[start+18:start+21]]
        s = set(temp)
        s.discard('.')
        if sum(1 for j in temp if j != '.') != len(s):
          return False
        start += 3
        
        
      return True
        