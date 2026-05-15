class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_characters = ['(','[','{']
        close_characters = [')',']','}']

        for c in s:
            if c in open_characters:
                stack.append(c)
            else:
                idx = close_characters.index(c)
                if stack and stack[-1] == open_characters[idx]:
                    stack.pop()
                else:
                    return False
        
        return not stack