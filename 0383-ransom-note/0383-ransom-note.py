class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        xd = {}
        for i in magazine:
            if i in xd:
                xd[i] += 1
            else:
                xd[i] = 1
        for i in ransomNote:
            if i in xd:
                xd[i] -= 1
            else:
                return False
        for i in xd.values():
            if i < 0:
                return False
        return True