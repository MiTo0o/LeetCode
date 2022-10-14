class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        xd = defaultdict(int)
        for i in nums:
            xd[i] += 1
        for i in xd:
            if xd[i] >= len(nums) / 2:
                return i
        