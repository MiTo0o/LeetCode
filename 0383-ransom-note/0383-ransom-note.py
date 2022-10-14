class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        xd = defaultdict(int)
        
        for i in magazine:
            xd[i] += 1
        for i in ransomNote:
            xd[i] -= 1
            

        return all([i >= 0 for i in xd.values()])