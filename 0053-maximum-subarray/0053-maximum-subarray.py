class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr, maxx = nums[0], nums[0]
        
        for i in nums[1:]:
            curr = max(curr, 0) + i
            maxx = max(maxx, curr)
        
        return maxx
        
        