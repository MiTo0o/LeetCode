class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != "0":
                    count += 1
                    self.helper(grid, i, j)
        return count
        
    def helper(self, grid, i, j):
        if grid[i][j] == "0":
            return
        
        grid[i][j] = "0"
        
        if i + 1 < len(grid):
            self.helper(grid, i + 1, j)
        if i - 1 >= 0:
            self.helper(grid, i - 1, j)
        if j + 1 < len(grid[i]):
            self.helper(grid, i, j + 1)
        if j - 1 >= 0:
            self.helper(grid, i, j - 1)