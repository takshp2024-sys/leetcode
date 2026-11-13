class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Split the version strings by '.' and convert each part to an integer
        v1 = [int(x) for x in version1.split('.')]
        v2 = [int(x) for x in version2.split('.')]
        
        n1, n2 = len(v1), len(v2)
        max_len = max(n1, n2)
        
        for i in range(max_len):
            # Get the revision values, defaulting to 0 if the index is out of bounds
            rev1 = v1[i] if i < n1 else 0
            rev2 = v2[i] if i < n2 else 0
            
            if rev1 < rev2:
                return -1
            elif rev1 > rev2:
                return 1
                
        # If all revisions are equal
        return 0