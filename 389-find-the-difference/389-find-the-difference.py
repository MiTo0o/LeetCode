class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ascii = 0
        for i in t:
          ascii += ord(i)
          
        for i in s:
          ascii -= ord(i)
          
        return chr(ascii)