from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Early exit optimization
        if len(ransomNote) > len(magazine):
            return False
            
        # Counter subtraction: returns an empty Counter if magazine has enough letters
        return not (Counter(ransomNote) - Counter(magazine))