"""
1. Approach
    - It is strictly required to write algorithm that uses only constant extra space.
    - So I set the variables, where should I put the character of length, which character I'm watching, how many characters I checked seqeuancially.
    - And also I append "0" before I iterate the `chars` to put character and length when it was the last index.
2. Time complexity : O(N) - Only need to scan the list `chars` once.
3. Space complexity : O(1) -  Only need `idx`, `c` and `cnt` to check how many characters in a row and which index should we put.
"""
class Solution:
    def compress(self, chars: List[str]) -> int:
        chars.append("0")
        idx = 0
        c = chars[0]
        cnt = 1
        for i in range(1, len(chars)):
            if chars[i-1] == chars[i]:
                cnt += 1
            else:
                chars[idx] = c
                c = chars[i]
                idx += 1
                if cnt != 1:
                    nums = list(str(cnt))
                    for num in nums:
                        chars[idx] = num
                        idx += 1
                cnt = 1

        chars = chars[:idx]
        return len(chars)      


        