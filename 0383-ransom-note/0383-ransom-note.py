class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        xd = {}
        
        for i in magazine:
            xd[i] = xd.get(i, 0) + 1
        for i in ransomNote:
            xd[i] = xd.get(i, 0) - 1
            
        for i in xd.values():
            if i < 0:
                return False
        return True