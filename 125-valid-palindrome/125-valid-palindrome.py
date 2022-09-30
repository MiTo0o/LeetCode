class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = "".join([c for c in s.lower() if c.isalnum()])
                
        return a == a[::-1]