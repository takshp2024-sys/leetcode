class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            new_s = []
            
            # Iterate through the string in steps of k
            for i in range(0, len(s), k):
                group = s[i:i+k]
                
                # Calculate the sum of the digits in the group
                group_sum = sum(int(char) for char in group)
                
                # Append the string representation of the sum to the new string
                new_s.append(str(group_sum))
                
            # Join the chunks to form the new string for the next round
            s = "".join(new_s)
            
        return s