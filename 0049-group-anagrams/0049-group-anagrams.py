class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary to map the sorted string (key) to a list of anagrams
        anagram_map = {}
        
        for s in strs:
            # Sort the string to create a common key for all anagrams
            # e.g., "eat", "tea", "ate" all sort to "aet"
            key = "".join(sorted(s))
            
            # If the key doesn't exist in the dictionary, initialize it with an empty list
            if key not in anagram_map:
                anagram_map[key] = []
                
            # Append the original string to the list of its anagrams
            anagram_map[key].append(s)
            
        # Return all the grouped lists
        return list(anagram_map.values())