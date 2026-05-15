class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Hash map for O(1) lookups and clean pair management
        bracket_map = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char not in bracket_map:
                # It's an opening bracket
                stack.append(char)
            else:
                # It's a closing bracket. Check the top of the stack safely.
                top_element = stack.pop() if stack else '#'
                if bracket_map[char] != top_element:
                    return False
                    
        return not stack