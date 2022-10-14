class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        xd = defaultdict(int)
        
        for i in magazine:
            xd[i] += 1
        for i in ransomNote:
            xd[i] -= 1
            if xd[i] < 0:
                return False

        return True