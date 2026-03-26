"""
1. Apporach
    - I thought we need to compare each rows and cols to check whether they contain the same elements
    - N is maximum 200 so, brute-force for checking each rows and col takes 2^4 * 10^7, slightly over 10^8 for 1 second.
2. Time Complexity : O(N^4) - As I said before. But too time spending actually.
3. Space Comeplexity : O(N) - Auxiliary space for column list.
"""
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        ans = 0
        for j in range(len(grid)):
            col = []
            for i in range(len(grid)):
                col.append(grid[i][j])
            
            for i in range(len(grid)):
                if col == grid[i]:
                    ans += 1
        
        return ans