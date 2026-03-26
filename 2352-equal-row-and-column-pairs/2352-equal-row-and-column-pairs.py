"""
1. Apporach
    - I use hash map, especially Counter class.
    - Put all posible numbers which row can make in `counter` with the number of occurance.
    - Make a query string with column and search that query in `counter`, if counter doesn't have query string, return 0
2. Time Complexity : O(n^2) - I wrote detailed explanations above the code 
3. Space Comeplexity : O(N) - For Counter and query stirng made with col need auxiliary space
"""
from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        ans = 0
        k = []
        # O(N^2) - every row, each elements in the row
        for row in grid:
            k.append(",".join(str(c) for c in row))
        # O(N)
        counter = Counter(k)

        # O(N^2)
        for j in range(len(grid)):
            col = []
            # O(N)
            for i in range(len(grid)):
                col.append(str(grid[i][j]))
            #O(N)
            col_string = ",".join(col)
            #O(1)
            ans += counter.get(col_string,0) # return 0 if there aren't col_string in counter

        return ans