class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ret = ""
        min_length = float('inf')
        for word in strs:
            min_length = min(min_length, len(word))

        if min_length == 0:
            return ret

        for i in range(min_length):
            c = strs[0][i]
            for word in strs:
                if word[i] != c:
                    return ret
            ret = ret + c
        
        return ret