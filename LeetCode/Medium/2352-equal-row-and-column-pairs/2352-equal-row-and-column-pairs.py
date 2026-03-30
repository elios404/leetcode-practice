"""
1. Approach :
    - Utilize a Hash Map to cache the frequency of each row for $O(1)$ lookups.
    - Because Python lists are unhashable, we cast each row into an immutable `tuple`.
    - We transpose the 2D matrix using the native `zip(*grid)` function, which cleanly yields each column as a tuple.
    - Iterate through the generated columns and increment our answer by the frequency of that tuple in our Hash Map.
2. Time Complexity : $O(N^2)$ - We traverse the $N \times N$ matrix twice: once to build the Counter, and once to query the columns.
3. Space Complexity : $O(N^2)$ - The Hash Map stores up to $N$ unique tuples of length $N$.
"""
from collections import Counter
from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # Step 1: Hash the rows as tuples. 
        # tuple(row) is vastly faster than ",".join(str(c))
        row_counter = Counter(tuple(row) for row in grid)
        
        ans = 0
        
        # Step 2: zip(*grid) transposes the matrix. 
        # It takes the 0th element of every row, groups them into a tuple, then the 1st, etc.
        for col in zip(*grid):
            # O(1) dictionary lookup using the tuple as the key
            ans += row_counter.get(col, 0)
            
        return ans