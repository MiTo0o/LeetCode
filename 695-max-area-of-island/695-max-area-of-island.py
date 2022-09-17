class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def helper(grid, i, j, size):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return
            size[0] += 1
            grid[i][j] = 0
            helper(grid, i + 1, j, size)
            helper(grid, i - 1, j, size)
            helper(grid, i, j + 1, size)
            helper(grid, i, j - 1, size)
        ans = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    size = [0]
                    helper(grid, i, j, size)
                    ans.append(size[0])
                
        return max(ans) if len(ans) > 0 else 0
