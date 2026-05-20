# I want to make a prefect algorithm code, but always make it with try and found error. I'm worried these kind of things are not good cuz
# In real world, it's hard to do test, can't keep submit easily, and also failure need money also.
# I want to be more stable developer

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_dict = {}
        word_dict = {}
        words = s.split(" ")

        # found from failure, failed submission
        if len(pattern) != len(words):
            return False

        #found from failure, failed submission
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