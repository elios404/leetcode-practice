from collections import deque

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c == "]":
                str_queue = deque()
                while stack[-1] != "[":
                    str_queue.appendleft(stack.pop())
                sub_str = "".join(str_queue)

                stack.pop() # remove "["

                cnt_queue = deque()
                while stack and stack[-1].isdigit():
                    cnt_queue.appendleft(stack.pop())
                cnt = int("".join(cnt_queue))

                stack.append(sub_str * cnt)
            else:
                stack.append(c)
                
        return "".join(stack)