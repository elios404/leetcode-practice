from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note_count = Counter(ransomNote)
        magazine_count = Counter(magazine)

        for k in note_count:
            if k not in magazine_count or note_count[k] > magazine_count[k]:
                return False

        return True