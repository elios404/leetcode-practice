"""
1. Approach : 
    - Firstly, we need to find which position (i, j) we can go in next step
    - If we need to check whether next move is heading right or left. By, gap between board_row and current row % 2 is even or odd.
    - If it's odd then need to go left, if it's even then go to right.
    - While heading right, if we reach the end of the row then go up, if heading left and reach the start of the row, then go up.
    => totally different apporach -> Why we need to think this in grid, we only need to know which number is in which position of the board (I solved in this way)
2. Time Complexity : O(N^2) - In worst case, visit every number in board
3. Space Complexity : O(N^2) - Visited Boolean Array is O(N) and queue for the next location.. Don't know well but at least smaller than put all the number in queue
"""
from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        # O(1)
        def findIndexFromNumber(num: int, n: int, m: int)->tuple:
            """
            number starts from 0 to n*m-1
            row and col start with 0
            """
            row = num // m
            col = num % m
            isRight = True if row % 2 == 0 else False

            if isRight:
                return (n - 1 - row, col)
            else:
                return (n - 1 - row, m - 1 - col)


        n = len(board) # row
        m = len(board[0]) # col
        visited = [False] * (n * m)

        q = deque()
        q.append((0, 0)) #number, count to reach there
        visited[0] = True

        # O(N)
        while q:
            curr = q.popleft()
            
            for move in range(1,7):
                next_num = curr[0] + move

                if next_num >= n*m: #out of range
                    continue

                index = findIndexFromNumber(next_num, n, m)
                short_track = board[index[0]][index[1]] - 1
                if short_track != -2:
                    next_num = short_track

                if visited[next_num]:
                    continue
                
                if next_num == n * m - 1:
                    return curr[1] + 1

                visited[next_num] = True #check visited into new position                
                q.append((next_num, curr[1] + 1))
            
        return -1