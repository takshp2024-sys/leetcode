class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        memo = {}
        
        def backtrack(start: int) -> List[str]:
            # If we have already computed the result for this index, return it
            if start in memo:
                return memo[start]
                
            # Base case: If we reached the end of the string, return an empty string
            # to signify a valid end of a sentence.
            if start == len(s):
                return [""]
                
            valid_sentences = []
            
            # Try all possible substrings starting from 'start'
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                
                # If the substring is a valid word
                if word in word_set:
                    # Recursively find valid sentences for the remaining string
                    next_sentences = backtrack(end)
                    
                    for next_sentence in next_sentences:
                        # If the next_sentence is empty, it means we are at the end
                        if next_sentence == "":
                            valid_sentences.append(word)
                        else:
                            # Otherwise, append the current word and a space before the next sentence
                            valid_sentences.append(word + " " + next_sentence)
                            
            # Save the result in memo before returning
            memo[start] = valid_sentences
            return valid_sentences
            
        return backtrack(0)