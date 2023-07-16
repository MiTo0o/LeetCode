from collections import defaultdict
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        old_count = defaultdict(int)
        for letter in s:
          old_count[letter] += 1
        
        new_count = defaultdict(int)
        for letter in t:
          new_count[letter] += 1
        
        for letter in new_count:
          if new_count[letter] != old_count[letter]:
            return letter