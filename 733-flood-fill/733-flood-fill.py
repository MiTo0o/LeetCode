class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        self.helper(image, sr, sc, image[sr][sc], newColor)
        return image
        
    def helper(self, image, row, col, old, new):
        if row < 0 or row >= len(image) or col < 0 or col >= len(image[0]) or image[row][col] != old or image[row][col] == new:
            return
        

        image[row][col] = new
        
        self.helper(image, row + 1, col, old, new)
        self.helper(image, row, col + 1, old, new)
        self.helper(image, row - 1, col, old, new)
        self.helper(image, row, col - 1, old, new)