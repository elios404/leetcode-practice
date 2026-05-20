class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_dict = {}
        word_dict = {}
        words = s.split(" ")

        if len(pattern) != len(words):
            return False

        for p, word in zip(pattern, words):
            # print(pattern_dict, word_dict)
            if p in pattern_dict and pattern_dict[p] != word:
                return False
            if word in word_dict and word_dict[word] != p:
                return False
            if p not in pattern_dict and word not in word_dict:
                pattern_dict[p] = word
                word_dict[word] = p
                continue
        
        return True