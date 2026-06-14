# What a clean and beautiful code..

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
            
        ret = []
        # zip(*strs) groups characters vertically. It auto-stops at the shortest string!
        for chars in zip(*strs):
            # A set removes duplicates. If the length is 1, all characters matched.
            if len(set(chars)) == 1:
                ret.append(chars[0])
            else:
                break
                
        return "".join(ret)