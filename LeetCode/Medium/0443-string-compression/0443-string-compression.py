"""
1. Approach
    - Implemented a Read/Write Two-Pointer technique to compree the array in-place.
    - The `read` pointer scans the array to count consecutive identical characters.
    - The `write` pointer sequentially overwrites the original array with the character and, if the count exceeds 1, its numeric frequency.
    - This structure natually handles the end of the array without requiring dummy appending.
2. Time complexity : O(N) - Both the read and write pointers traverse the array exactly once in a single forward direction.
3. Space complexity : O(1) - The compression is performed in-place using only constant integer pointers.
"""
class Solution:
    def compress(self, chars: List[str]) -> int:
        read = 0
        write = 0
        n = len(chars)

        while read < n:
            current_char = chars[read]
            count = 0

            while read < n and chars[read] == current_char:
                read += 1
                count += 1
            
            chars[write] = current_char
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        
        return write