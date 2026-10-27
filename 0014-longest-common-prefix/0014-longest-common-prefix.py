class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # If the array is empty, there is no common prefix
        if not strs:
            return ""
        
        # Start by assuming the first string is the common prefix
        prefix = strs[0]
        
        # Compare the prefix with every other string in the array
        for i in range(1, len(strs)):
            # While the current string does not start with the prefix,
            # shorten the prefix by removing the last character
            while not strs[i].startswith(prefix):
                prefix = prefix[:-1]
                # If the prefix becomes empty, there is no common prefix
                if not prefix:
                    return ""
                    
        return prefix