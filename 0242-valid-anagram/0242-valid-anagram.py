from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths differ, they can't be anagrams
        if len(s) != len(t):
            return False
            
        return Counter(s) == Counter(t)