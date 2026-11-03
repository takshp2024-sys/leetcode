class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # s.split() automatically handles multiple spaces and leading/trailing spaces
        words = s.split()

        # Return the length of the last word
        return len(words[-1])
